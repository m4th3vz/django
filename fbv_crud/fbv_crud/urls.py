from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='tarefa_listar'),
    path('criar/', views.criar, name='tarefa_criar'),
    path('atualizar/<int:id>/', views.atualizar, name='tarefa_atualizar'),
    path('apagar/<int:id>/', views.apagar, name='tarefa_apagar'),
]
