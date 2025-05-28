from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarefa
from .forms import TarefaFormulario

def listar(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'fbv_crud/tarefa_listar.html', {'object_list': tarefas})

def criar(request):
    if request.method == "POST":
        form = TarefaFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefa_listar')
    else:
        form = TarefaFormulario()
    return render(request, 'fbv_crud/tarefa_criar.html', {'form': form, 'view': {'object': {}}})  # pk vazio para "Criar"

def atualizar(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    if request.method == "POST":
        form = TarefaFormulario(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('tarefa_listar')
    else:
        form = TarefaFormulario(instance=tarefa)
    return render(request, 'fbv_crud/tarefa_criar.html', {'form': form, 'view': {'object': tarefa}})

def apagar(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('tarefa_listar')
    return render(request, 'fbv_crud/tarefa_confirmar_deletar.html', {'tarefa': tarefa})
