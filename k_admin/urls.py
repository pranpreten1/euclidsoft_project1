from django.urls import path
from k_admin import views


urlpatterns = [
    path('', views.module_list, name='module_list'),
]