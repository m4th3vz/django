from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
    TemplateView, RedirectView, FormView, View
)
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Todo
from .forms import ContactForm

# ListView: Usada para exibir uma lista de objetos de um modelo.
class TodoListView(ListView):
    model = Todo
    template_name = "cbv_app/todo_list.html"

    # Esta view lista todas as instâncias do modelo Todo.
    # - model = Todo → especifica o modelo cujos objetos serão listados.
    # - template_name → define qual template será usado para renderizar a lista.

    # O Django busca automaticamente todos os objetos do modelo e os envia ao template na variável `object_list`.
    # No template, é possível iterar sobre essa lista usando `{% for todo in object_list %}`.
    # Caso queira personalizar o nome da variável, pode-se usar `context_object_name = "nome_desejado"`.


# DetailView: Usada para exibir os detalhes de um único objeto de um modelo.
class TodoDetailView(DetailView):
    model = Todo
    template_name = "cbv_app/todo_detail.html"

    # Esta view mostra as informações completas de uma instância específica do modelo Todo.
    # - model = Todo → indica que o objeto a ser exibido é do modelo Todo.
    # - template_name → define o template para renderizar os detalhes do objeto.

    # O Django recupera o objeto automaticamente com base no parâmetro da URL (normalmente `pk` ou `slug`).
    # No template, o objeto está disponível como `object` (ou com nome personalizado usando `context_object_name`).


# CreateView: Usada para criar um novo objeto de um modelo.
class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "description", "deadline"]
    success_url = reverse_lazy("todo_list")
    template_name = "cbv_app/todo_form.html"

    # Esta view exibe um formulário para criar uma nova instância do modelo Todo.
    # - model = Todo → define o modelo que será criado.
    # - fields → lista dos campos do modelo que aparecerão no formulário.
    # - success_url → URL para onde o usuário será redirecionado após a criação bem-sucedida (neste caso, a lista de tarefas).
    # - template_name → template usado para renderizar o formulário.

    # Quando o formulário é enviado e validado com sucesso, o Django salva o novo objeto automaticamente.
    # CreateView simplifica o processo de criação, evitando que você precise escrever código para salvar o formulário manualmente.


# UpdateView: Usada para editar/atualizar um objeto existente de um modelo.
class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "description", "deadline"]
    success_url = reverse_lazy("todo_list")
    template_name = "cbv_app/todo_form.html"

    # Esta view exibe um formulário pré-preenchido com os dados de uma instância do modelo Todo para edição.
    # - model = Todo → define o modelo que será atualizado.
    # - fields → lista dos campos do modelo que aparecerão no formulário para edição.
    # - success_url → URL para onde o usuário será redirecionado após a atualização bem-sucedida (neste caso, a lista de tarefas).
    # - template_name → template usado para renderizar o formulário de edição (geralmente o mesmo do CreateView).

    # O Django recupera o objeto automaticamente com base no parâmetro da URL (normalmente `pk`).
    # Ao enviar o formulário e validar, o objeto é atualizado automaticamente no banco de dados.


# DeleteView: Usada para deletar um objeto existente de um modelo.
class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")
    template_name = "cbv_app/todo_confirm_delete.html"

    # Esta view exibe uma página de confirmação para deletar uma instância do modelo Todo.
    # - model = Todo → define o modelo do objeto a ser deletado.
    # - success_url → URL para onde o usuário será redirecionado após a deleção (neste caso, a lista de tarefas).
    # - template_name → template usado para exibir a confirmação de deleção.

    # O Django recupera o objeto automaticamente com base no parâmetro da URL (normalmente `pk`).
    # Ao confirmar (geralmente via método POST), o objeto é removido do banco de dados.
    # DeleteView facilita a criação de fluxos seguros para exclusão de dados com confirmação prévia.


# TemplateView: Usada para renderizar um template simples com contexto opcional.
class HomePageView(TemplateView):
    template_name = "cbv_app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mensagem"] = "Bem-vindo à página inicial!"
        return context

    # Esta view renderiza a página inicial com um template estático ou semi-dinâmico.
    # - template_name → define qual template será usado para renderizar a página.

    # O método get_context_data é sobrescrito para adicionar dados ao contexto do template.
    # Neste caso, adiciona a variável "mensagem" com o texto "Bem-vindo à página inicial!".
    # Essa variável pode ser acessada no template via {{ mensagem }}.

    # TemplateView é ideal para páginas simples que não precisam de manipulação de banco de dados.


# RedirectView: Usada para redirecionar o usuário para outra URL.
class RedirecionarView(RedirectView):
    url = reverse_lazy("todo_list")

    # Esta view redireciona automaticamente para a URL nomeada "todo_list".
    # - url → define a URL de destino do redirecionamento usando reverse_lazy para evitar problemas na importação.

    # Quando acessada, essa view não exibe template, apenas redireciona o usuário imediatamente.
    # Útil para simplificar rotas que só precisam encaminhar para outra página.


# FormView: Usada para exibir e processar formulários que não necessariamente estão ligados a um modelo.
class ContatoView(FormView):
    template_name = "cbv_app/contato.html"
    form_class = ContactForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # Esta view exibe o formulário ContactForm e processa os dados enviados.
    # - template_name → template que renderiza o formulário.
    # - form_class → classe do formulário que será usado (ContactForm).
    # - success_url → URL para onde o usuário será redirecionado após o envio e validação correta do formulário.

    # O método form_valid é sobrescrito para executar ações adicionais quando o formulário é válido.
    # Aqui, ele imprime os dados limpos (cleaned_data) no console, depois continua o fluxo padrão.
    # FormView facilita a manipulação de formulários genéricos, cuidando da renderização e validação.


# View: Classe base genérica para criar views personalizadas.
class MinhaViewPersonalizada(View):
    def get(self, request):
        return redirect("home")

    # Esta view personalizada sobrescreve o método GET para redirecionar o usuário para a URL nomeada "home".
    # - get(self, request) → método que responde às requisições GET.
    # - redirect("home") → redireciona imediatamente para a página "home".

    # Útil quando se deseja controlar manualmente o comportamento da view sem usar as views genéricas do Django.
