from Emp_app import views
from django.urls import path

urlpatterns = [

    path('', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('save_employee/', views.save_employee, name='save_employee'),
    path('add_dynamic_field/', views.add_dynamic_field, name='add_dynamic_field'),


   
]