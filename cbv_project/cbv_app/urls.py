from django.urls import path
from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("todo/", TodoListView.as_view(), name="todo_list"),
    path("todo/<int:pk>/", TodoDetailView.as_view(), name="todo_detail"),
    path("todo/novo/", TodoCreateView.as_view(), name="todo_create"),
    path("todo/<int:pk>/editar/", TodoUpdateView.as_view(), name="todo_update"),
    path("todo/<int:pk>/deletar/", TodoDeleteView.as_view(), name="todo_delete"),
    path("redirecionar/", RedirecionarView.as_view(), name="redirecionar"),
    path("contato/", ContatoView.as_view(), name="contato"),
    path("minha-view/", MinhaViewPersonalizada.as_view(), name="minha_view"),
]
