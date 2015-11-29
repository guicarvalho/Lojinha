# coding: utf-8

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout as logout_, login as login_
from django.http import JsonResponse
from django.shortcuts import redirect

from core.forms import LoginForm


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


def login(request):
    form = LoginForm(request.POST)

    message = {}

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
                    message = {'message': 'Login realizado com sucesso !', 'level': 'success'}
                else:
                    message = {'message': 'Seu usuário foi desativo !', 'level': 'danger'}
            else:
                message = {'message': 'Seu usuário ou senha estão incorretos !', 'level': 'danger'}
        else:
            response = JsonResponse(form.errors)
            response.status_code = 500
            return response

        return JsonResponse(message)


def logout(request):
    logout_(request)

    messages.info(request, 'Logout realizado !')

    return redirect('home_page')
