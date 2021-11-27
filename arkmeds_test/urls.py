from django.urls import path
from . import views

urlpatterns = [
    path('create_call_for_equipments', views.create_call_for_equipment, name='create_call_for_equipments'),
]
