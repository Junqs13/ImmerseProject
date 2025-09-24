from django.contrib import admin
from .models import Video, Question, Choice, UserProgress

# Register your models here.

# Esta linha diz ao Django: "Eu quero que o modelo Video apareça na área de admin."
admin.site.register(Video)

# Fazemos o mesmo para os modelos Question e Choice
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(UserProgress)