from django.urls import path
from .views import MeuEndpointView

urlpatterns = [
    path('meu-endpoint/', MeuEndpointView.as_view()),
]
