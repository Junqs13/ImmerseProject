from django.core.management.base import BaseCommand
from core.models import Category

class Command(BaseCommand):
    help = 'Cria um conjunto inicial de categorias para os vídeos.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Criando categorias iniciais...'))

        categories = [
            'Conversação',
            'Gramática',
            'Cultura',
            'Negócios (Business)',
            'Nível Iniciante',
            'Nível Intermediário',
            'Nível Avançado',
        ]

        for category_name in categories:
            category, created = Category.objects.get_or_create(name=category_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Categoria "{category.name}" criada.'))
            else:
                self.stdout.write(self.style.WARNING(f'Categoria "{category.name}" já existe.'))

        self.stdout.write(self.style.SUCCESS('Processo de criação de categorias finalizado.'))