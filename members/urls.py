from django.urls import path
from .views import UserRegisterView, UserEditForm

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditForm.as_view(), name='edit_profile'),
]
