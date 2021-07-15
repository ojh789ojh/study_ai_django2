from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from account.views import hello_world, AccountCreate, AccountDetail

app_name = 'account'

urlpatterns = [
    path('hello_world/', hello_world, name="hello_world"),
    path('create/', AccountCreate.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', AccountDetail.as_view(), name='detail'),
]
