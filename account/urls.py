

from django.urls import path
from .views import UserRegistrationView
from django.views.generic import TemplateView

urlpatterns = [
    path(
        "",TemplateView.as_view(template_name="account/index.html"),name="index",
    ),
    path('register/', UserRegistrationView.as_view(), name='register'),
]
