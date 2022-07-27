from django.urls import path
from .views import UserRegisterView, UserEditForm, PasswordsChangeView
from . import views

# from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditForm.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success/', views.password_success, name='password_success'),

]
