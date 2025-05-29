from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarefa
from .forms import TarefaFormulario

# listar: Visão para exibir a lista de tarefas (Listagem)
def listar(request):
    lista_tarefas = Tarefa.objects.all()
    return render(request, 'fbv_crud/tarefa_listar.html', {'lista_tarefas': lista_tarefas}) # A primeira parte ('lista_tarefas') é a chave que será usada dentro do template, e a segunda parte (lista_tarefas) é a variável Python que você criou na view.

# Esta função recupera todas as tarefas do banco usando .objects.all().
# Em seguida, renderiza o template 'tarefa_listar.html', passando os dados no contexto como 'lista_tarefas'.
# - request → objeto da requisição HTTP.
# - render → função que combina o template com os dados e retorna a resposta.
# A variável 'lista_tarefas' será usada no template para iterar sobre as tarefas.
# Esta função é equivalente à classe ListView nas CBVs.


# criar: Visão para criar uma nova tarefa (Criação)
def criar(request):
    if request.method == "POST":
        formulario = TarefaFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarefa_listar')
    else:
        formulario = TarefaFormulario()
    return render(request, 'fbv_crud/tarefa_criar.html', {'formulario': formulario, 'visao': {'objeto': {}}})

# Esta visão trata tanto a exibição quanto o envio do formulário.
# - Se a requisição for POST, os dados são usados para preencher o formulário.
#   - Se for válido, salva a nova tarefa e redireciona para a listagem.
# - Se for GET, exibe o formulário vazio.
# O template 'tarefa_criar.html' recebe:
# - 'formulario' → o formulário para ser exibido no HTML.
# - 'visao': {'objeto': {}} → compatível com templates usados também em CBVs, que esperam 'visao.objeto'.
# Esta função é equivalente à classe CreateView nas CBVs.


# atualizar: Visão para editar uma tarefa existente (Atualização)
def atualizar(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    if request.method == "POST":
        formulario = TarefaFormulario(request.POST, instance=tarefa)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarefa_listar')
    else:
        formulario = TarefaFormulario(instance=tarefa)
    return render(request, 'fbv_crud/tarefa_criar.html', {'formulario': formulario, 'visao': {'objeto': tarefa}})

# Esta visão busca a tarefa pelo ID fornecido.
# - get_object_or_404 → retorna o objeto ou lança erro 404 se não existir.
# - Se a requisição for POST, preenche o formulário com os dados enviados e associa à tarefa existente.
#   - Se for válido, salva as alterações e redireciona.
# - Se for GET, exibe o formulário preenchido com os dados atuais.
# Usa o mesmo template 'tarefa_criar.html' para criação e edição.
# - 'formulario' → formulário exibido.
# - 'visao': {'objeto': tarefa} → compatível com templates de CBVs.
# Esta função é equivalente à classe UpdateView nas CBVs.


# apagar: Visão para excluir uma tarefa (Exclusão)
def apagar(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('tarefa_listar')
    return render(request, 'fbv_crud/tarefa_confirmar_deletar.html', {'tarefa': tarefa})

# Busca a tarefa pelo ID.
# - Se for POST, confirma que o usuário clicou em "Confirmar" e deleta a tarefa.
#   - Após deletar, redireciona para a listagem.
# - Se for GET, exibe o template de confirmação 'tarefa_confirmar_deletar.html'.
# - 'tarefa' → usada no template para mostrar os dados da tarefa a ser excluída.
# Esta função é equivalente à classe DeleteView nas CBVs.
