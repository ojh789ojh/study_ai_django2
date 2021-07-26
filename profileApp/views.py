from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileApp.forms import ProfileCreationForm
from profileApp.models import Profile


class ProfileCreationView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('account:hello_world')
    template_name = 'profile/create.html'
