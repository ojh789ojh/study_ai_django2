from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileApp.decorators import profile_ownership_required
from profileApp.forms import ProfileCreationForm
from profileApp.models import Profile


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProfileCreationView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('account:hello_world')
    template_name = 'profile/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('account:hello_world')
    template_name = 'profile/update.html'
