from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('<int:id>/', views.Employee_Detail, name='employee',),
]
