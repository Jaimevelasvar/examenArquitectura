from .views import *
from django.urls import path, include 
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('home', home,name='home'),
    path('', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('transaccion',transaccion, name='transaccion'),
    path('reportes',reportes, name='reportes'),
    path('historial',historial, name='historial'),
]
