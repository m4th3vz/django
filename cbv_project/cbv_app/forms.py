from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(max_length=100)
    mensagem = forms.CharField(widget=forms.Textarea)
