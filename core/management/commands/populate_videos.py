# Código para populate_videos.py
from django.core.management.base import BaseCommand
from core.models import Video

class Command(BaseCommand):
    help = 'Popula o banco de dados com uma lista inicial de 10 vídeos verificados.'

    def handle(self, *args, **options):
        self.stdout.write('Iniciando o cadastro de vídeos...')
        videos_list = [
            {'title': 'Do schools kill creativity?', 'description': 'Sir Ken Robinson faz um caso divertido e profundo para a criação de um sistema educacional que nutre (em vez de minar) a criatividade. (Palestra TED)', 'video_url': 'https://www.youtube.com/watch?v=iG9CE55wbtY'},
            {'title': 'What makes a good life? Lessons from the longest study on happiness', 'description': 'O que nos mantém felizes e saudáveis ao longo da vida? Robert Waldinger compartilha os resultados de um estudo de 75 anos. (Palestra TED)', 'video_url': 'https://www.youtube.com/watch?v=8KkKuTCFvzI'},
            {'title': 'A Simple Guide to Cooking Pasta | SORTEDfood', 'description': 'Um guia básico e divertido sobre como cozinhar macarrão, com vocabulário de culinária e instruções claras.', 'video_url': 'https://www.youtube.com/watch?v=tVoT6J3_5eA'},
            {'title': 'The Egg - A Short Story', 'description': 'Uma animação do Kurzgesagt baseada em um conto de Andy Weir. Ótimo para vocabulário narrativo e filosófico.', 'video_url': 'https://www.youtube.com/watch?v=h6fcK_fRYaI'},
            {'title': 'How to sound smart in your TEDx Talk', 'description': 'Will Stephen mostra de forma cômica como a forma de falar pode soar mais importante que o conteúdo. Ótimo para entonação e linguagem corporal.', 'video_url': 'https://www.youtube.com/watch?v=8S0FDjFBj8o'},
            {'title': 'The Lord of the Rings - Official Trailer', 'description': 'Um trailer de filme com narração épica e diálogos curtos. Bom para treinar a audição em um contexto de fantasia.', 'video_url': 'https://www.youtube.com/watch?v=x8UAUAuKNcU'},
            {'title': 'What would happen if you didn’t sleep?', 'description': 'Claudia Aguirre, da TED-Ed, detalha os efeitos da privação de sono no corpo e cérebro. Vocabulário científico e de saúde.', 'video_url': 'https://www.youtube.com/watch?v=_y5h4X4Jk2Q'},
            {'title': 'Learn English with The Fresh Prince of Bel-Air', 'description': 'Uma análise de cenas do seriado "Um Maluco no Pedaço" para aprender inglês coloquial, gírias e humor dos anos 90.', 'video_url': 'https://www.youtube.com/watch?v=qcIup_y_wFk'},
            {'title': 'How to Tie a Tie (Mirrored / Slowly) - The Windsor Knot', 'description': 'Um tutorial prático e lento sobre como dar um nó em uma gravata. Excelente para seguir instruções passo a passo.', 'video_url': 'https://www.youtube.com/watch?v=xAg7z6u4NE8'},
            {'title': 'What is writer\'s block?', 'description': 'Um vídeo da Vox que explora o bloqueio criativo. Bom para vocabulário relacionado a psicologia e criatividade.', 'video_url': 'https://www.youtube.com/watch?v=ATHp_b-3F2M'},
        ]
        for video_data in videos_list:
            video, created = Video.objects.get_or_create(title=video_data['title'], defaults=video_data)
            if created: self.stdout.write(self.style.SUCCESS(f'Vídeo "{video.title}" cadastrado.'))
        self.stdout.write(self.style.SUCCESS('Cadastro de vídeos finalizado!'))