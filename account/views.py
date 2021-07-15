from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

from account.models import HelloWorld


def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get("input_text")

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        hello_world_list = HelloWorld.objects.all()
        return HttpResponseRedirect(reverse('account:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'account/hello_world.html', context={'text': 'GET METHOD!',
                                                                    'hello_world_list': hello_world_list})


class AccountCreate(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('account:hello_world')
    template_name = 'account/create.html'


class AccountDetail(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'account/detail.html'
