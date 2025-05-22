from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
    TemplateView, RedirectView, FormView, View
)
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Todo
from .forms import ContactForm

class TodoListView(ListView):
    model = Todo
    template_name = "cbv_app/todo_list.html"

class TodoDetailView(DetailView):
    model = Todo
    template_name = "cbv_app/todo_detail.html"

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "description", "deadline"]
    success_url = reverse_lazy("todo_list")
    template_name = "cbv_app/todo_form.html"

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "description", "deadline"]
    success_url = reverse_lazy("todo_list")
    template_name = "cbv_app/todo_form.html"

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")
    template_name = "cbv_app/todo_confirm_delete.html"

class HomePageView(TemplateView):
    template_name = "cbv_app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mensagem"] = "Bem-vindo à página inicial!"
        return context

class RedirecionarView(RedirectView):
    url = reverse_lazy("todo_list")

class ContatoView(FormView):
    template_name = "cbv_app/contato.html"
    form_class = ContactForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class MinhaViewPersonalizada(View):
    def get(self, request):
        return redirect("home")
