# core/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('videos/', views.all_videos_view, name='all_videos'),
    path('categoria/<str:category_name>/', views.category_view, name='category_view'),
    path('video/<int:pk>/', views.video_detail, name='video_detail'),
    path('check-answer/', views.check_answer, name='check_answer'),
    path('sobre/', views.pagina_sobre, name='pagina_sobre'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='video_list'), name='logout'),
    path('register/', views.register, name='register'),
    path('perfil/', views.profile_view, name='profile_view'),
    path('save-progress/', views.save_progress, name='save_progress'),
    path('subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
]