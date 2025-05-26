from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(max_length=100)
    mensagem = forms.CharField(widget=forms.Textarea)

# forms.py: Define formulários usados para entrada e validação de dados do usuário.

# Os formulários podem ser baseados em modelos (ModelForm) ou independentes (Form).
# Eles controlam como os dados são apresentados nas páginas HTML, além de validar e limpar os dados recebidos.
# Usar formulários ajuda a garantir que os dados enviados pelo usuário estejam corretos antes de serem processados.
# Também facilita a criação de formulários complexos e a reutilização de regras de validação.
