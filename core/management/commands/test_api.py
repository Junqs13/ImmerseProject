from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError

try:
    # Importa as duas funções helper do models.py
    from core.models import check_video_embeddable, get_video_id_from_url
except ImportError:
    print("ERRO: Não foi possível encontrar 'check_video_embeddable' ou 'get_video_id_from_url' no core/models.py")
    check_video_embeddable = None
    get_video_id_from_url = None

# Esta é a lista de URLs do seu script setup_data.py
# Copiamos ela para cá para o teste ser completo.
VIDEO_URLS_PARA_TESTAR = [
    {'title': 'Do schools kill creativity?', 'url': 'https://www.youtube.com/watch?v=iG9CE55wbtY'},
    {'title': 'What makes a good life? Lessons from the longest study on happiness', 'url': 'https://www.youtube.com/watch?v=8KkKuTCFvzI'},
    {'title': 'A Simple Guide to Cooking Pasta | SORTEDfood', 'url': 'https://youtu.be/slLGniM_mJA?si=Z6V8xxkeEqXMuVEH'},
    {'title': 'The Egg - A Short Story', 'url': 'https://www.youtube.com/watch?v=h6fcK_fRYaI'},
    {'title': 'How to sound smart in your TEDx Talk', 'url': 'https://www.youtube.com/watch?v=8S0FDjFBj8o'},
    {'title': 'The Lord of the Rings - Official Trailer', 'url': 'https://www.youtube.com/watch?v=x8UAUAuKNcU'},
    {'title': 'What would happen if you didn’t sleep?', 'url': 'https://youtu.be/dqONk48l5vY?si=NhbcuidiNB_7E4SR'},
    {'title': 'Learn English with The Fresh Prince of Bel-Air', 'url': 'https://youtu.be/rAMvLi4wGhI?si=_7_kGQmMDYNWCUHP'},
    {'title': 'How to Tie a Tie (Mirrored / Slowly) - The Windsor Knot', 'url': 'https://www.youtube.com/watch?v=xAg7z6u4NE8'},
    {'title': 'What is writer\'s block?', 'url': 'https://youtu.be/rcKtcXbjwD4?si=N8eB3ZjMI4hF-MDy'},
    {'title': 'The surprising habits of original thinkers | Adam Grant', 'url': 'https://www.youtube.com/watch?v=fxbCHn6gE3U'},
    {'title': 'How a handful of tech companies control billions of minds every day | Tristan Harris', 'url': 'https://youtu.be/C74amJRp730?si=nxA4B4SdAotcnsSk'},
    {'title': 'Your brain on video games | Daphne Bavelier', 'url': 'https://youtu.be/FktsFcooIG8?si=xbIlk8r5VjUkoIO_'},
    {'title': 'How to speak so that people want to listen | Julian Treasure', 'url': 'https://www.youtube.com/watch?v=eIho2S0ZahI'},
    {'title': 'What if we detonated a nuke in the Marianas Trench?', 'url': 'https://youtu.be/A7eb1DHZ9GQ?si=Q5wpAeYPoAVCqWof'},
    {'title': 'The rise and fall of the Inca Empire - Gordon McEwan', 'url': 'https://www.youtube.com/watch?v=UO5ktwPXsyM'},
    {'title': 'How do cancer cells behave differently from healthy ones? - George Zaidan', 'url': 'https://youtu.be/BmFEoCFDi-w?si=xcRuiEEFtnxG6U1S'},
    {'title': 'Why does the Leaning Tower of Pisa lean? - Alex Gendler', 'url': 'https://youtu.be/HFqf6aKdOC0?si=6q7-2_rdsa5qHah5'},
    {'title': 'What gives a dollar bill its value? - Doug Levinson', 'url': 'https://youtu.be/XNu5ppFZbHo?si=Qmz8Z0mSNXkD1ji2'},
    {'title': 'The first secret of great design | Tony Fadell', 'url': 'https://www.youtube.com/watch?v=9uOMectkCCs'},
]


class Command(BaseCommand):
    help = 'Testa a função de verificação da API do YouTube em TODOS os 20 vídeos do projeto.'

    def handle(self, *args, **options):
        if not check_video_embeddable or not get_video_id_from_url:
            self.stdout.write(self.style.ERROR("Funções do models.py não importadas. Verifique o models.py."))
            return

        self.stdout.write(self.style.NOTICE(f"--- Iniciando teste de validação em {len(VIDEO_URLS_PARA_TESTAR)} vídeos ---"))
        
        bloqueados = 0
        permitidos = 0

        for video_info in VIDEO_URLS_PARA_TESTAR:
            title = video_info['title']
            url = video_info['url']
            video_id = get_video_id_from_url(url)
            
            if not video_id:
                self.stdout.write(self.style.ERROR(f"[FALHA] '{title}' - Não foi possível extrair o ID da URL: {url}"))
                continue

            try:
                is_embeddable, reason = check_video_embeddable(video_id)
                
                if is_embeddable:
                    self.stdout.write(self.style.SUCCESS(f"[PERMITIDO] '{title}'"))
                    permitidos += 1
                else:
                    self.stdout.write(self.style.ERROR(f"[BLOQUEADO] '{title}' (ID: {video_id}) - Motivo: {reason}"))
                    bloqueados += 1

            except ValidationError as e:
                self.stdout.write(self.style.ERROR(f"[ERRO API] '{title}' (ID: {video_id}) - {e}"))
                bloqueados += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"[ERRO GERAL] '{title}' (ID: {video_id}) - {e}"))
                bloqueados += 1

        self.stdout.write(self.style.NOTICE(f"\n--- Teste Concluído ---"))
        self.stdout.write(self.style.SUCCESS(f"Vídeos Permitidos: {permitidos}"))
        self.stdout.write(self.style.ERROR(f"Vídeos Bloqueados: {bloqueados}"))