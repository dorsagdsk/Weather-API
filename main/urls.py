from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.login_page, name='login'),
    path('cities/', views.cities_list_view, name='cities_list'),

]
