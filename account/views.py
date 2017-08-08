# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from account.forms import RegisterUserForm


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = "account/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseForbidden()

        return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return HttpResponse('User registered')