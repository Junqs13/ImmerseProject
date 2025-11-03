from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

# --- NOVOS IMPORTS ---
from django.conf import settings
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import re # Import para extrair o ID
# ---------------------


# -----------------------------
# FUNÇÃO HELPER (Fora da classe)
# -----------------------------

def get_video_id_from_url(url):
    """Extrai o ID do vídeo de diferentes formatos de URL do YouTube."""
    if 'watch?v=' in url:
        return url.split('v=')[-1].split('&')[0]
    elif 'youtu.be/' in url:
        return url.split('/')[-1].split('?')[0]
    elif '/embed/' in url:
        return url.split('/embed/')[-1].split('?')[0]
    return None

def check_video_embeddable(video_id):
    """
    Verifica se um vídeo do YouTube pode ser incorporado usando a API.
    Checa tanto o status 'embeddable' quanto restrições de região.
    """
    if not settings.YOUTUBE_API_KEY:
        raise ValidationError("A YOUTUBE_API_KEY não está configurada no settings.py")
        
    try:
        youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)
        request = youtube.videos().list(
            # AGORA PEDIMOS 2 PARTES: status E contentDetails
            part="status,contentDetails",
            id=video_id
        )
        response = request.execute()

        if not response.get('items'):
            # Vídeo não encontrado
            raise ValidationError(f"Vídeo com ID '{video_id}' não foi encontrado no YouTube.")
            
        item = response['items'][0]
        status = item.get('status', {})
        details = item.get('contentDetails', {})

        # --- CHECAGEM 1: A mais óbvia (Erro 153) ---
        if not status.get('embeddable', False):
            return False, "Incorporação desativada pelo proprietário"

        # --- CHECAGEM 2: Bloqueio de Região ---
        restriction = details.get('regionRestriction')
        if restriction:
            # Se 'allowed' existe, o vídeo SÓ pode ser visto nesses países.
            # Se 'BR' (Brasil) não estiver na lista, bloqueamos.
            if 'allowed' in restriction and 'BR' not in restriction['allowed']:
                return False, f"Não permitido para a região BR (só permitido em: {restriction['allowed']})"
            
            # Se 'blocked' existe, o vídeo NÃO pode ser visto nesses países.
            # Se 'BR' (Brasil) estiver na lista, bloqueamos.
            if 'blocked' in restriction and 'BR' in restriction['blocked']:
                return False, f"Bloqueado para a região BR"

        # Se passou nas duas checagens, está liberado!
        return True, "Permitido"

    except HttpError as e:
        # Trata erros de API (ex: cota excedida, API desativada)
        raise ValidationError(f"Erro ao verificar vídeo na API do YouTube: {e}")
    except Exception as e:
        # Outros erros
        raise ValidationError(f"Erro inesperado na verificação do vídeo: {e}")


# -----------------------------
# Modelo para Categorias
# -----------------------------
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


# -----------------------------
# Modelo para Vídeos (COM MUDANÇAS)
# -----------------------------
class Video(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    video_url = models.URLField(max_length=255, verbose_name="URL do Vídeo")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Enviado em")
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Categoria")

    def __str__(self):
        return self.title

    def get_video_id(self):
        # Usa a função helper que criamos
        return get_video_id_from_url(self.video_url)

    @property
    def embed_url(self):
        video_id = self.get_video_id()
        if video_id:
            return f'https://www.youtube.com/embed/{video_id}'
        return self.video_url

    @property
    def thumbnail_url(self):
        video_id = self.get_video_id()
        if video_id:
            return f'https://img.youtube.com/vi/{video_id}/hqdefault.jpg'
        return ''

    def clean(self):
        if "youtube.com" not in self.video_url and "youtu.be" not in self.video_url:
            raise ValidationError("Insira um link válido do YouTube.")

    def save(self, *args, **kwargs):
        video_id = self.get_video_id()
        
        if not video_id:
             raise ValidationError("Não foi possível extrair o ID do vídeo da URL.")

        # Só verifica na criação (quando self.pk é None)
        if not self.pk:
            is_embeddable, reason = check_video_embeddable(video_id)
            if not is_embeddable:
                raise ValidationError(f"O vídeo '{self.title}' (ID: {video_id}) não pode ser salvo. Motivo: {reason}")
        
        # Normaliza a URL
        self.video_url = f'https://www.youtube.com/embed/{video_id}'
        super().save(*args, **kwargs)


# -----------------------------
# Modelos (Perguntas, Alternativas, Progresso, etc.)
# ... O RESTO DO ARQUIVO CONTINUA EXATAMENTE IGUAL ...
# -----------------------------
class Question(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="questions", verbose_name="Vídeo")
    question_text = models.CharField(max_length=255, verbose_name="Texto da Pergunta")
    explanation = models.TextField(blank=True, null=True, verbose_name="Explicação da Resposta Correta")

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices", verbose_name="Pergunta")
    choice_text = models.CharField(max_length=100, verbose_name="Texto da Alternativa")
    is_correct = models.BooleanField(default=False, verbose_name="É a correta?")

    def __str__(self):
        return self.choice_text

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    score = models.CharField(max_length=10)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'video')

    def __str__(self):
        return f'{self.user.username} - {self.video.title} - Pontuação: {self.score}'

class Testimonial(models.Model):
    author_name = models.CharField(max_length=100, verbose_name="Nome do Autor")
    testimonial_text = models.TextField(verbose_name="Texto da Avaliação")
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)],
        verbose_name="Avaliação (1 a 5 estrelas)"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

    def __str__(self):
        return f'Avaliação de {self.author_name}'

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name="E-mail")
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Inscrição")

    def __str__(self):
        return self.email