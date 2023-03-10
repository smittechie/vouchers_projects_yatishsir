from django.urls import path, include

from . import views
import django.contrib.auth.views as auth

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('signup/', views.SignupFormView.as_view(), name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', auth.LogoutView.as_view(), name='logout'),
    path('voucherlist/<int:pk>/', views.Voucher_Detail.as_view(), name='voucher'),
    path('employeelist/<int:id>/', views.Employee_Detail, name='employee', ),
    path('employeelist/', views.Employeelist.as_view(), name='employeelist'),
    path('voucherlist/', views.Voucherlist.as_view(), name='voucherlist'),
    path('voucherallotment/', views.VoucherallotmentView.as_view(), name='voucherallotment'),
    path('voucherallotment/<int:pk>/', views.Voucherallotment_to_id_View.as_view(), name='voucherallotment_to_id_View'),

]