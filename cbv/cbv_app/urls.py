from django.urls import path
from .views import *

urlpatterns = [
    # URL raiz: exibe a página inicial com HomePageView
    path("", HomePageView.as_view(), name="home"),
    
    # Lista todas as tarefas com TodoListView
    path("todo/", TodoListView.as_view(), name="todo_list"),
    
    # Mostra detalhes de uma tarefa específica pelo seu PK com TodoDetailView
    path("todo/<int:pk>/", TodoDetailView.as_view(), name="todo_detail"),
    
    # Página para criar uma nova tarefa com TodoCreateView
    path("todo/novo/", TodoCreateView.as_view(), name="todo_create"),
    
    # Página para editar uma tarefa existente identificada pelo PK com TodoUpdateView
    path("todo/<int:pk>/editar/", TodoUpdateView.as_view(), name="todo_update"),
    
    # Página para confirmar e deletar uma tarefa pelo PK com TodoDeleteView
    path("todo/<int:pk>/deletar/", TodoDeleteView.as_view(), name="todo_delete"),
    
    # Redireciona para a lista de tarefas com RedirecionarView
    path("redirecionar/", RedirecionarView.as_view(), name="redirecionar"),
    
    # Página com formulário de contato usando ContatoView
    path("contato/", ContatoView.as_view(), name="contato"),
    
    # Exemplo de view personalizada que redireciona para a home com MinhaViewPersonalizada
    path("minha-view/", MinhaViewPersonalizada.as_view(), name="minha_view"),
]
