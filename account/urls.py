from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from account.views import *

app_name = 'account'

urlpatterns = [
    path('create/', AccountCreate.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', AccountDetail.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdate.as_view(), name='update'),
    path('delete/<int:pk>', AccountDelete.as_view(), name='delete'),
]
