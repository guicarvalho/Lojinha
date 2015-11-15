# coding: utf-8

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _

from client.forms import AddressForm, ClientForm
from core.forms import LoginForm


def create_client(request):
    client_form = ClientForm(request.POST, request.FILES)
    address_form = AddressForm(request.POST)

    if request.method == 'POST':
        if address_form.is_valid() and client_form.is_valid():
            client = client_form.save(commit=False)
            address = address_form.save(commit=False)

            # Verifica se usuário já existe
            if not User.objects.filter(username=client.email).exists():
                # Cria usuário para acessar o sistema
                User.objects.create_user(username=client.email, email=client.email,
                                         password=request.POST.get('password'),
                                         first_name=client.first_name)

                # Insere o cliente e endereço no banco
                client.save()
                address.client = client
                address.save()

                messages.success(request, _('Usuário criado com sucesso !'))
                return redirect('home_page')

            messages.add_message(request, messages.ERROR,
                                 _('Já existe usuário cadastrado com esse e-mail !'), extra_tags='danger')
    else:
        client_form = ClientForm()
        address_form = AddressForm()

    return render(request, 'client/client_form.html', {
        'client_form': client_form,
        'address_form': address_form,
        'login_form': LoginForm()
    })
