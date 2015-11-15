# coding: utf-8

from django.contrib import messages
from django.contrib.auth import authenticate, login as login_
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _

from core.forms import LoginForm


def login(request):
    form = LoginForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            # Autentica o usuário
            usuario = authenticate(username=form.cleaned_data.get('username'),
                                   password=form.cleaned_data.get('password'))

            # Verifica se o usuário existe
            if usuario is not None:
                # Verifica se o usuário está ativo
                if usuario.is_active:
                    login_(request, usuario)
                    messages.success(request, 'Login realizado com sucesso !')
                else:
                    messages.add_message(request, messages.ERROR,
                                         _('Seu usuário foi desativo !'), extra_tags='danger')
            else:
                messages.add_message(request, messages.ERROR,
                                     _('Seu usuário ou senha estão incorretos !'), extra_tags='danger')
        else:
            return JsonResponse(form.errors)

        return redirect('home_page')
