from django.urls import path
from .views import *

urlpatterns = [
    path("", Listar.as_view(), name="tarefa_listar"),
    path("criar", Criar.as_view(), name="tarefa_criar"),
    path("atualizar/<int:pk>", Atualizar.as_view(), name="tarefa_atualizar"),
    path("apagar/<int:pk>", Apagar.as_view(), name="tarefa_apagar"),
]
