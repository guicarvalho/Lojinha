# coding: utf-8

from django.http import HttpResponse

from django.views.generic import View


class Cart(View):

    def post(self, request, *args, **kwargs):
        print (request)
        print (args)
        print (kwargs)
        return HttpResponse('Teste')
