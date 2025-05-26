from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todo_list, name="todo_list"),
    path("todos/<int:pk>/", views.todo_detail, name="todo_detail"),
    path("todos/criar/", views.todo_create, name="todo_create"),
    path("todos/<int:pk>/editar/", views.todo_update, name="todo_update"),
    path("todos/<int:pk>/deletar/", views.todo_delete, name="todo_delete"),
    path("todos/<int:pk>/completar/", views.todo_complete, name="todo_complete"),
    path("contato/", views.contato, name="contato"),
    path("redir/", views.redirecionar, name="redirecionar"),
]
