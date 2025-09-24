# core/urls.py
from django.urls import path
# Importando as views de autenticação prontas do Django
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('video/<int:pk>/', views.video_detail, name='video_detail'),
    path('check-answer/', views.check_answer, name='check_answer'),
    path('sobre/', views.pagina_sobre, name='pagina_sobre'),

    # --- NOVAS ROTAS DE AUTENTICAÇÃO ---
    # Rota de Login: Usa a LoginView pronta do Django. Só precisamos dizer qual template usar.
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),

    # Rota de Logout: Usa a LogoutView. next_page diz para onde redirecionar após o logout.
    path('logout/', auth_views.LogoutView.as_view(next_page='video_list'), name='logout'),

    # Rota de Cadastro: Aponta para uma view que vamos criar chamada 'register'.
    path('register/', views.register, name='register'),
    
    path('save-progress/', views.save_progress, name='save_progress'),

]