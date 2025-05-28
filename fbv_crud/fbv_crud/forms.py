from django import forms
from .models import Tarefa

class TarefaFormulario(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'prazo']
