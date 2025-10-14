# core/management/commands/populate_testimonials.py
from django.core.management.base import BaseCommand
from core.models import Testimonial

class Command(BaseCommand):
    help = 'Cria 10 avaliações (testimonials) de exemplo.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Limpando avaliações antigas...'))
        Testimonial.objects.all().delete()

        testimonials = [
            {'author_name': 'Carlos Silva', 'testimonial_text': 'Plataforma incrível! A imersão com vídeos realmente funciona e os quizzes ajudam a fixar o conteúdo.', 'rating': 5},
            {'author_name': 'Juliana Pereira', 'testimonial_text': 'O método é muito mais divertido que os cursos tradicionais. Sinto que meu "listening" melhorou muito em poucas semanas.', 'rating': 5},
            {'author_name': 'Fernando Costa', 'testimonial_text': 'Adorei a seleção de vídeos. Temas atuais e relevantes que me mantêm engajado no aprendizado.', 'rating': 4},
            {'author_name': 'Beatriz Almeida', 'testimonial_text': 'A funcionalidade de salvar o progresso e ver meu perfil é muito motivadora. Recomendo!', 'rating': 5},
            {'author_name': 'Lucas Martins', 'testimonial_text': 'Finalmente uma ferramenta que foca em entender o inglês do dia a dia. As explicações do quiz são ótimas.', 'rating': 5},
            {'author_name': 'Gabriela Souza', 'testimonial_text': 'O site é rápido, bonito e funciona perfeitamente no celular. A experiência do usuário é excelente.', 'rating': 5},
            {'author_name': 'Rafael Oliveira', 'testimonial_text': 'Gostei muito das categorias. Consigo focar nos vídeos de "Business English" que são importantes para minha carreira.', 'rating': 4},
            {'author_name': 'Mariana Lima', 'testimonial_text': 'Simples, direto ao ponto e eficaz. É o que eu precisava para destravar meu inglês.', 'rating': 5},
            {'author_name': 'Thiago Santos', 'testimonial_text': 'O modo escuro é um toque de classe! Mostra o cuidado com os detalhes. A plataforma como um todo é fantástica.', 'rating': 5},
            {'author_name': 'Ana Clara Rocha', 'testimonial_text': 'A melhor parte é aprender com conteúdo real, não com diálogos fabricados. Faz toda a diferença na compreensão.', 'rating': 5},
        ]

        for item in testimonials:
            Testimonial.objects.create(**item)

        self.stdout.write(self.style.SUCCESS(f'{len(testimonials)} avaliações foram criadas com sucesso!'))