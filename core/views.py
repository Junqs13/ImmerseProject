import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Importando o nosso formulário customizado e removendo o antigo
from .forms import CustomUserCreationForm

# Imports dos nossos Modelos
from .models import Video, Choice, UserProgress


def video_list(request):
    """
    Exibe a lista de todos os vídeos e seleciona o mais recente como destaque.
    """
    all_videos = Video.objects.all().order_by('-uploaded_at')
    featured_video = all_videos.first()

    context = {
        'videos': all_videos,
        'featured_video': featured_video,
    }
    return render(request, 'core/video_list.html', context)


def video_detail(request, pk):
    """
    Exibe a página de detalhes para um vídeo específico, incluindo o questionário.
    Também verifica se o usuário já completou este quiz para exibir o progresso.
    """
    video = get_object_or_404(Video, pk=pk)
    user_progress = None
    
    # Se o usuário estiver logado, tenta buscar o progresso dele para este vídeo
    if request.user.is_authenticated:
        try:
            user_progress = UserProgress.objects.get(user=request.user, video=video)
        except UserProgress.DoesNotExist:
            user_progress = None # Nenhum progresso encontrado

    # Criamos o dicionário com os dados para o JavaScript
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
    """
    Verifica se uma alternativa escolhida está correta.
    Usado pelo JavaScript para dar feedback em tempo real. Responde em JSON.
    """
    choice_id = request.GET.get('choice_id')
    is_correct = False
    try:
        choice = Choice.objects.get(pk=choice_id)
        is_correct = choice.is_correct
    except Choice.DoesNotExist:
        is_correct = False
    
    return JsonResponse({'is_correct': is_correct})


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