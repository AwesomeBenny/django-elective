from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
    path('details/<int:pk>', views.details, name='details'),
    path('', views.index, name='index'),
]
