from django import forms
from .models import Todo

class ContactForm(forms.Form):
    nome = forms.CharField(max_length=100)
    mensagem = forms.CharField(widget=forms.Textarea)

# fbv_app/forms.py
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "deadline"]
