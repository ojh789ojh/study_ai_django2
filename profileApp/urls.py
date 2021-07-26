from django.urls import path

from profileApp.views import ProfileCreationView

app_name = 'profile'

urlpatterns = [
    path('create/', ProfileCreationView.as_view(), name='create'),
]