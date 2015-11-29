# coding: utf-8

from django import forms
from django.utils.translation import ugettext_lazy as _

from client.models import Address, Client


class ClientForm(forms.ModelForm):
    SEX_CHOICES = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    ]

    photo = forms.ImageField(label=_('Foto'))
    birthday = forms.DateField(label=_('Data de Nasicimento'),
                               widget=forms.TextInput(attrs={'class': 'form-control input_md',
                                                             'type': 'date'}))
    sex = forms.ChoiceField(widget=forms.RadioSelect, choices=SEX_CHOICES)
    password = forms.CharField(label='Senha',
                               widget=forms.PasswordInput(attrs={'class': 'form-control input_md'}))
    confirm_password = forms.CharField(label='Confirme sua senha',
                                       widget=forms.PasswordInput(attrs={'class': 'form-control input_md'}))
    country = forms.CharField(initial=_('Brasil'), required=False)
    client = forms.ModelChoiceField(queryset=Client.objects.all(), required=False)

    def clean(self):
        cleaned_data = super(ClientForm, self).clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('password', _('As senhas informadas não são iguais'))

    class Meta:
        model = Client
        fields = '__all__'

        labels = {
            'first_name': _('Nome'),
            'last_name': _('Sobrenome'),
            'cpf_cnpj': _('CPF/CNPJ'),
            'email': _('E-mail'),
            'phone': _('Telefone'),
            'cell_phone': _('Celular'),
            'nickname': _('Apelido'),
            'sex': _('Sexo'),
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control input_md',
                'placeholder': _('Informe seu nome')
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control input_md',
                'placeholder': _('Informe seu sobrenome')
            }),
            'cpf_cnpj': forms.TextInput(attrs={
                'class': 'form-control input_md',
                'placeholder': _('Informe seu CPF/CNPJ')
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control input_md',
                'placeholder': _('Informe seu e-mail')
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control input_md',
                'placeholder': _('Informe seu telefone')
            }),
            'cell_phone': forms.TextInput(attrs={
                'class': 'form-control input_md',
                'placeholder': _('Informe seu celular')
            }),
            'nickname': forms.TextInput(attrs={
                'class': 'form-control input_md',
                'placeholder': _('Informe seu apelido')
            })
        }


class AddressForm(forms.ModelForm):
    BR_STATES = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', u'Amapá'), ('AM', 'Amazonas'),
        ('BA', 'Bahia'), ('CE', u'Ceará'), ('DF', 'Distrito Federal'),
        ('ES', u'Espírito Santo'), ('GO', u'Goiás'), ('MA', u'Maranhão'),
        ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'), ('PA', u'Pará'), ('PB', u'Paraíba'),
        ('PR', u'Paraná'), ('PE', 'Pernambuco'), ('PI', u'Piauí'),
        ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'), ('RO', u'Rondônia'), ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'), ('SP', u'São Paulo'), ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    ]

    state = forms.ChoiceField(label=_('Estado'),
                              choices=[('', 'Informe seu estado')] + BR_STATES,
                              widget=forms.Select(
                              attrs={'class': 'form-control'}
                              ))

    class Meta:
        model = Address
        fields = '__all__'

        labels = {
            'zip_code': _('CEP'),
            'street': _('Logradouro'),
            'number': _(u'Número'),
            'complement': _('Complemento'),
            'neigthboor': _('Bairro'),
            'city': _('Cidade'),
        }

        widgets = {
            'street': forms.TextInput(attrs={
                'class': 'form-control input_md',
                'placeholder': _('Informe seu logradouro')
            }),
            'number': forms.TextInput(attrs={
                'class': 'form-control input_md',
                'placeholder': _(u'Informe o número'),
                'type': 'number'
            }),
            'complement': forms.TextInput(attrs={
                'class': 'form-control input_md',
                'placeholder': _('Informe o complemento')
            }),
            'neigthboor': forms.TextInput(attrs={
                'class': 'form-control input_md', 'placeholder': _('Informe seu bairro')
            }),
            'zip_code': forms.TextInput(attrs={
                'class': 'form-control input_md',
                'placeholder': _('Informe seu CEP'),
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control input_md',
                'placeholder': _('Informe sua cidade')
            }),
        }
