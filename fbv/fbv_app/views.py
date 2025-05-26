from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .models import Todo
from .forms import ContactForm, TodoForm
from datetime import date

# Página inicial
def home(request):
    mensagem = "Bem-vindo à página inicial!"
    return render(request, "fbv_app/home.html", {"mensagem": mensagem})

# Página de detalhes
def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, "fbv_app/todo_detail.html", {"todo": todo})

# Lista de tarefas
def todo_list(request):
    todos = Todo.objects.all().order_by('deadline')
    return render(request, "fbv_app/todo_list.html", {"object_list": todos})

# Criar tarefa
def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = TodoForm()
    return render(request, "fbv_app/todo_form.html", {"form": form})

# Atualizar tarefa
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = TodoForm(instance=todo)
    return render(request, "fbv_app/todo_form.html", {"form": form})

# Deletar tarefa
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        todo.delete()
        return redirect("todo_list")
    return render(request, "fbv_app/todo_confirm_delete.html", {"object": todo})

# Marcar como completa
def todo_complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if not todo.finished_at:
        todo.finished_at = date.today()
        todo.save()
    return redirect("todo_list")

# Contato (formulário)
def contato(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("home")
    else:
        form = ContactForm()
    return render(request, "fbv_app/contato.html", {"form": form})

# Redirecionamento simples
def redirecionar(request):
    return redirect("todo_list")
