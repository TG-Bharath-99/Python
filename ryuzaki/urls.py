from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('display/', views.emp_details, name='employees'),
    path('add/', views.add_employee, name='add'),
    path('update/<int:id>/', views.update_employee, name='update'),
    path('delete/<int:id>/', views.delete_employee, name='delete'),
]