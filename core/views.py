import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import NewsletterSubscriber
from .forms import CustomUserCreationForm

import random
from .models import Video, Choice, UserProgress, Category, Testimonial


# core/views.py
def video_list(request):
    all_videos = Video.objects.select_related('category').order_by('-uploaded_at')
    featured_video = all_videos.first()

    # Lógica para as avaliações aleatórias
    all_testimonials = list(Testimonial.objects.all())
    random_testimonials = []
    if len(all_testimonials) >= 3:
        random_testimonials = random.sample(all_testimonials, 3)

    # --- LINHA DE DIAGNÓSTICO ---
    print(f"!!! DIAGNÓSTICO: A view encontrou {len(all_testimonials)} avaliações no total e selecionou {len(random_testimonials)} aleatoriamente.")
    # ----------------------------

    context = {
        'videos': all_videos[:9],
        'featured_video': featured_video,
        'page_title': 'Últimos Vídeos',
        'is_homepage': True,
        'random_testimonials': random_testimonials,
    }
    return render(request, 'core/video_list.html', context)

def category_view(request, category_name):
    # Encontra o objeto da categoria. Se não existir, retorna erro 404.
    category = get_object_or_404(Category, name=category_name)

    # Filtra os vídeos que pertencem a essa categoria
    videos_in_category = Video.objects.filter(category=category).order_by('-uploaded_at')

    context = {
        'videos': videos_in_category,
        # Não temos um vídeo em destaque aqui, mas podemos adicionar um título dinâmico à página
        'featured_video': None, 
        'page_title': f'Vídeos da Categoria: {category.name}'
    }

    # Reutiliza o mesmo template da página inicial!
    return render(request, 'core/video_list.html', context)


def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    user_progress = None
    
    if request.user.is_authenticated:
        try:
            user_progress = UserProgress.objects.get(user=request.user, video=video)
        except UserProgress.DoesNotExist:
            user_progress = None
    
    # Criamos o dicionário com os dados aqui na view
    js_data_dict = {
        'videoId': video.pk,
        'totalQuestions': video.questions.count(),
    }

    context = {
        'video': video,
        'user_progress': user_progress,
        'js_data': js_data_dict, # E passamos ele para o contexto
    }
    return render(request, 'core/video_detail.html', context)


def pagina_sobre(request):
    """
    Renderiza a página estática "Sobre".
    """
    return render(request, 'core/sobre.html')


def register(request):
    """
    Gerencia o cadastro de novos usuários usando o nosso formulário customizado.
    """
    if request.method == 'POST':
        # Usa nosso formulário customizado
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        # Mostra uma instância em branco do nosso formulário
        form = CustomUserCreationForm()
    
    context = {'form': form}
    return render(request, 'core/register.html', context)


def check_answer(request):
    choice_id = request.GET.get('choice_id')

    try:
        # Pega a alternativa que o usuário escolheu
        user_choice = Choice.objects.get(pk=choice_id)
        # Pega a pergunta relacionada a essa alternativa
        question = user_choice.question
        # Pega a alternativa correta para essa pergunta
        correct_choice = question.choices.get(is_correct=True)

        # Prepara os dados para enviar de volta como JSON
        data = {
            'user_choice_is_correct': user_choice.is_correct,
            'correct_choice_id': correct_choice.pk,
            'explanation': question.explanation,
        }
    except (Choice.DoesNotExist, Question.DoesNotExist):
        return JsonResponse({'error': 'Opção ou pergunta não encontrada'}, status=404)

    return JsonResponse(data)


@login_required
@require_POST
def save_progress(request):
    """
    Salva a pontuação final de um usuário para um vídeo.
    Requer que o usuário esteja logado e que a requisição seja do tipo POST.
    """
    data = json.loads(request.body)
    video_id = data.get('video_id')
    score = data.get('score')
    total_questions = data.get('total_questions')

    video = get_object_or_404(Video, id=video_id)

    # Usa update_or_create para evitar duplicatas.
    progress, created = UserProgress.objects.update_or_create(
        user=request.user,
        video=video,
        defaults={'score': f'{score}/{total_questions}'}
    )

    return JsonResponse({'status': 'success', 'message': 'Progresso salvo com sucesso!'})




@login_required
def profile_view(request):
    
    user_progress = UserProgress.objects.filter(user=request.user).order_by('-completed_at')
    
    context = {
        'progress_list': user_progress
    }
    
    return render(request, 'core/profile.html', context)

def all_videos_view(request):
    # 1. Pega TODOS os vídeos do banco de dados
    videos = Video.objects.all().order_by('-uploaded_at')

    # 2. Prepara o contexto para o template
    context = {
        'page_title': 'Todos os Vídeos', # Um título para a página
        'videos': videos,
        'is_homepage': False # Flag para indicar que NÃO é a homepage
    }

    # 3. Reutiliza o template da página inicial
    return render(request, 'core/video_list.html', context)

def newsletter_subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            # O get_or_create evita erros se o e-mail já estiver cadastrado
            NewsletterSubscriber.objects.get_or_create(email=email)

    # Redireciona o usuário de volta para a página onde ele estava
    return redirect(request.META.get('HTTP_REFERER', '/'))