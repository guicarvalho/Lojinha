# coding: utf-8

from django.views.generic import TemplateView

from core.views import LoginRequiredMixin
from client.models import Client


class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = 'purchase/checkout_form.html'

    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)

        username = self.request.user.email

        context['client'] = Client.objects.get(email=username)

        return context
