from django.urls import path, include
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/',UserRegisterView.as_view(), name='signup'),
    path('edit_profile/',UserEditView.as_view(), name='edit_profile'),
    path('login/',include('django.contrib.auth.urls'), name='login'),
    path('password/',PasswordsChangeView.as_view(template_name = 'registration/change_password.html')),
    path('password_success/', views.password_success, name='password_success'),
    path('<int:pk>/profile/',ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/',EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profil_page')
    
]
 
