from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    # 1. Adicionamos os novos campos que queremos
    first_name = forms.CharField(max_length=30, required=True, label="Nome")
    last_name = forms.CharField(max_length=150, required=True, label="Sobrenome")
    email = forms.EmailField(max_length=254, required=True, label="Email")

    class Meta(UserCreationForm.Meta):
        model = User
        # 2. Definimos a ordem dos campos, adicionando os novos
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # 3. Traduzimos os campos originais do formulário
        self.fields['username'].label = "Nome de Usuário"
        # As senhas são um caso especial, usamos password1 e password2
        self.fields['password1'].label = "Senha"
        self.fields['password2'].label = "Confirmação de Senha"

        # Adicionando classes do Bootstrap para deixar os campos mais bonitos
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs = {'class': 'form-control'}