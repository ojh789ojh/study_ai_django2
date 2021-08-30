from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from account.decorator import account_ownership_required
from account.form.form import AccountCreationForm


class AccountCreate(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('articleApp:list')
    template_name = 'account/create.html'


class AccountDetail(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'account/detail.html'


has_ownership = [login_required(login_url=reverse_lazy('account:login')), account_ownership_required]


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdate(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    template_name = 'account/update.html'

    def get_success_url(self):
        return reverse('accountApp:detail', kwargs={'pk': self.user.pk})


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDelete(DeleteView):
    model = User
    context_object_name = 'target_user'
    template_name = 'account/delete.html'
    success_url = reverse_lazy('articleApp:list')

