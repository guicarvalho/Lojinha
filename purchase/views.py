# coding: utf-8

from django.views.generic import TemplateView

from core.views import LoginRequiredMixin


class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = 'purchase/checkout_form.html'

    def get_context_data(self, **kwargs):
        pass
