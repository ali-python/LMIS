# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.views.generic import TemplateView, RedirectView, UpdateView, ListView
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db.models import Sum
from django.utils import timezone
from django.http import HttpResponseRedirect,HttpResponse
from .models import UserProfile
from django.db import transaction



class LoginView(FormView):
    template_name = 'login.html'
    form_class = auth_forms.AuthenticationForm

    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)
        return HttpResponseRedirect(reverse('common:home'))

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid(form)

    # def get_context_data(self, **kwargs):
    #     context = super(LoginView, self).get_context_data(**kwargs)
    #     try:
    #         admin_config = AdminConfiguration.objects.get(id=1)
    #         context.update({
    #             'config': admin_config
    #         })
    #     except AdminConfiguration.DoesNotExist:
    #         pass
    #     return context


class LogoutView(RedirectView):

    def dispatch(self, request, *args, **kwargs):
        auth_logout(self.request)
        return super(LogoutView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('common:login'))


class HomePageView(TemplateView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            HomePageView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context


class UserListView(ListView):
    template_name = 'users_accounts/user_list.html'
    paginate_by = 100
    model = UserProfile
    ordering = '-id'

class RegisterView(FormView):
    form_class = auth_forms.UserCreationForm
    template_name = 'users_accounts/user_register.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            RegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        with transaction.atomic():
            user = form.save()
            user_profile = UserProfile.objects.create(user = user)

            user_profile.phone_no = self.request.POST.get(
                'phone')
            user_profile.user_type = self.request.POST.get(
                'user_type')
            user_profile.address = self.request.POST.get(
                'address')
            user_profile.office_address = self.request.POST.get(
                'office_address')
            user_profile.city = self.request.POST.get(
                'city')
            user_profile.picture = self.request.POST.get(
                'picture')
            user_profile.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            auth_user = authenticate(username=username,password=raw_password)
            auth_login(self.request, auth_user)

        return HttpResponseRedirect(reverse('common:user_list'))

    def form_invalid(self, form):
        print(form.errors)
        print("___________________________________")
        print("___________________________________")
        print("___________________________________")
        print("___________________________________")
        return super(RegisterView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        if self.request.POST:
            context.update({
                'username': self.request.POST.get('username'),
                'phone': self.request.POST.get('phone_no'),
                'password1': self.request.POST.get('password1'),
                'password2': self.request.POST.get('password2')
            })
        return context