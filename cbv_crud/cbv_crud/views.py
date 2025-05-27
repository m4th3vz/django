from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Tarefa


class Listar(ListView):
    model = Tarefa
    template_name = "cbv_crud/tarefa_listar.html"


class Criar(CreateView):
    model = Tarefa
    fields = ["titulo", "descricao", "prazo"]
    success_url = reverse_lazy("tarefa_listar")
    template_name = "cbv_crud/tarefa_criar.html"


class Atualizar(UpdateView):
    model = Tarefa
    fields = ["titulo", "descricao", "prazo"]
    success_url = reverse_lazy("tarefa_listar")
    template_name = "cbv_crud/tarefa_criar.html"


class Apagar(DeleteView):
    model = Tarefa
    success_url = reverse_lazy("tarefa_listar")
    template_name = "cbv_crud/tarefa_confirmar_deletar.html"
