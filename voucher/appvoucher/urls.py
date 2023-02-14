from django.urls import path, include

from . import views
import django.contrib.auth.views as auth

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginForm.as_view(), name='login'),
    path('logout/', auth.LogoutView.as_view(), name='logout'),
    path('<str:name>/', views.Voucher_Detail.as_view(), name='voucher'),
    path('<int:id>/', views.Employee_Detail, name='employee', ),

]