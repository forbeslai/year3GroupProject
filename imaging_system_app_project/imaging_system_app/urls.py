from django.urls import path
from imaging_system_app import views

app_name = 'imaging_system_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('customers/', views.customers, name='customers'),
    path('bills/', views.bills, name='bills'),
]