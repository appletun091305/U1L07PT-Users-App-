from django.urls import path
from . import views
app_name = 'users'

urlpatterns = [
    path('', views.register, name = "users"),
    path('register', views.register, name = "register"),
]