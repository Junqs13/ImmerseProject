from django.db import models
from django.contrib.auth.models import User

# Modelo para os Vídeos
class Video(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    video_url = models.URLField(max_length=255, verbose_name="URL do Vídeo")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Enviado em")

    def __str__(self):
        return self.title

    @property
    def embed_url(self):
        """
        Converte uma URL normal do YouTube ('watch?v=') em uma URL de incorporação ('embed/').
        Isso cria um "campo virtual" que pode ser usado nos templates.
        """
        if 'watch?v=' in self.video_url:
            # Extrai o ID do vídeo, mesmo que hajam outros parâmetros na URL
            video_id = self.video_url.split('v=')[-1].split('&')[0]
            return f'https://www.youtube.com/embed/{video_id}'
        # Retorna a URL original se não for o formato esperado, para outros tipos de vídeo
        return self.video_url

# Modelo para as Perguntas do quiz
class Question(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="questions", verbose_name="Vídeo")
    question_text = models.CharField(max_length=255, verbose_name="Texto da Pergunta")

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