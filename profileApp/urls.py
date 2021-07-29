from django.urls import path

from profileApp.views import ProfileCreationView, ProfileUpdateView

app_name = 'profile'

urlpatterns = [
    path('create/', ProfileCreationView.as_view(), name='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
]