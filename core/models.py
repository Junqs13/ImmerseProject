from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Modelo para os Vídeos
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome")

    class Meta:
        # Corrige o plural de "Categoria" no painel de admin
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name
# core/models.py
class Video(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    video_url = models.URLField(max_length=255, verbose_name="URL do Vídeo")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Enviado em")
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Categoria")

    def __str__(self):
        return self.title

    def get_video_id(self):
        """Extrai o ID do vídeo de diferentes formatos de URL do YouTube."""
        if 'watch?v=' in self.video_url:
            return self.video_url.split('v=')[-1].split('&')[0]
        elif 'youtu.be/' in self.video_url:
            return self.video_url.split('/')[-1].split('?')[0]
        elif '/embed/' in self.video_url:
            return self.video_url.split('/embed/')[-1].split('?')[0]
        return None

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
        return '' # Retorna vazio se não conseguir extrair o ID
class Question(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="questions", verbose_name="Vídeo")
    question_text = models.CharField(max_length=255, verbose_name="Texto da Pergunta")
    explanation = models.TextField(blank=True, null=True, verbose_name="Explicação da Resposta Correta")

    def __str__(self):
        return self.question_text

# Modelo para as Alternativas de cada pergunta
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices", verbose_name="Pergunta")
    choice_text = models.CharField(max_length=100, verbose_name="Texto da Alternativa")
    is_correct = models.BooleanField(default=False, verbose_name="É a correta?")

    def __str__(self):
        return self.choice_text

# Modelo para o Progresso do Usuário
class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    # Usamos CharField para armazenar a pontuação no formato "X/Y"
    score = models.CharField(max_length=10)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Garante que um usuário só tenha uma entrada de pontuação por vídeo
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