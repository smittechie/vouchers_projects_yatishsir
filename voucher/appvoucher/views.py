from itertools import count

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import SignUpForm, LogInForm, Voucherallotment_to_id_Form
from .models import Employee, Voucher
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.db.models import F


# Create your views here.
class Home(TemplateView):
    template_name = 'appvoucher/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['employee'] = Employee.objects.all()
        context['voucher'] = Voucher.objects.all()
        return context

    # extra_context = {'vouch': Voucher.objects.all()}            ##this is for extra context in data


# @login_required(login_url='login/')
class Voucher_Detail(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Voucher


class Voucherlist(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'appvoucher/voucher_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Voucherlist, self).get_context_data(*args, **kwargs)
        context['voucher'] = Voucher.objects.all()
        return context


@login_required(login_url='login')
def Employee_Detail(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        employee = None
    # context = {'employee': employee}
    # context = employee
    print(employee)
    return render(request, 'appvoucher/employee_detail.html', {'context': employee})


class Employeelist(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'appvoucher/employee_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Employeelist, self).get_context_data(*args, **kwargs)
        context['employee'] = Employee.objects.all()
        print(context)
        return context


# class VoucherallotmentView(LoginRequiredMixin,TemplateView):
#     login_url = '/login/'
#     template_name = 'appvoucher/voucherallotment.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(VoucherallotmentView, self).get_context_data(*args, **kwargs)
#         context['employee'] = Employee.objects.all()
#         context['voucher'] = Voucher.objects.all()
#         return context


class VoucherallotmentView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Employee
    queryset = Employee.objects.all()
    context_object_name = 'employee'
    # form_class = Voucherallotment
    template_name = 'appvoucher/voucherallotment.html'
    # success_url = 'home/'


""" Voucher alloted to the employe id """


class Voucherallotment_to_id_View(UpdateView):
    model = Employee
    # fields = [
    #      "voucher",
    # ]
    success_url = '/'
    form_class = Voucherallotment_to_id_Form

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()  ## id of the employee
        # print(self.object.id)
        # print("id of the employee  ")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        v_list = request.POST.getlist("voucher")  ##giving the list of the vouchers
        # vouchers = Voucher.objects.filter(id__in=v_list)  ## id of boucher in list
        vouchers = Voucher.objects.all()
        # for voucher_detail in vouchers:
        #     print(voucher_detail.quantity)
        # print(vouchers)
        # print("current voucherrrrrr")
        current_emp = Employee.objects.get(id=self.get_object().id)
        for i in v_list:
            current_emp = Employee.objects.get(id=self.get_object().id)
            total = Employee.objects.filter(voucher__id=i).count()
            for voucher_detail in vouchers:
                if  total <= voucher_detail.quantity:
                    print("yes")
                else:
                    print("nooo")
        return super().post(request, *args, **kwargs)


""" Try to add and delete voucher  """


# if vouchers:
#     current_emp = Employee.objects.get(id = self.get_object().id)
#     for v in vouchers:
#         # print(self.get_object())                                          ##getting current user email
#         # employee = self.get_object().id                                     ##getting the current id
#         # current_emp = Employee.objects.get(id = self.get_object().id)
#         current_emp.voucher.add(v)
#         current_emp.save()
#         # Employee.objects.filter(id=self.get_object().id).update(voucher=F('voucher') + v)     ##trying new
#         v.quantity -= 1
#         v.save()
# else:
#     for v in Voucher.objects.exclude(id__in=v_list):
#         v.quantity += 1
#         v.save()
#
# emp = Employee.objects.get(id=kwargs.get("pk"))
# emp.voucher.set(v_list)
# return super().post(request, *args, **kwargs)


# def signup_form(self,request):
#     data = SignUpForm()
#     return render(request, template_name='appvoucher/login.html')


class SignupFormView(CreateView):
    template_name = 'appvoucher/signup.html'
    form_class = SignUpForm

    # success_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        print(request.POST)

        if form.is_valid():
            Employee.objects.create_user(**form.cleaned_data)
            return HttpResponseRedirect(reverse_lazy('login'))
        return render(request, 'appvoucher/signup.html', {'form': form})


'''Trying user creation form '''

# class SignupView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'appvoucher/signup.html'


""" Login Form """


def login_user(request):
    if request.POST:
        form = AuthenticationForm(request.POST)
        print(request.POST)
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        # form = LogInForm(request.POST)
        # if form.is_valid():
        #     # error_message =
        #     # print(form.cleaned_data)
        #     user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))

        # if user is None:
        #     return render(request, "appvoucher/login.html")
        # else:
        #     # print(user)
        #     messages.error(request, 'username or password not correct')
        #     login(request, user)
        # return redirect("home")

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'username or password not correct')
            return redirect('login')
    context = {'form': LogInForm}
    return render(request, "appvoucher/login.html", context)

# class LoginView(View):
#     def get(self, request, *args, **kwargs):
#         context = {
#             "form": LogInForm()
#         }
#         return render(request, 'appvoucher/login.html', context)
# #     form_class =
# #     context_object_name = "form"


# def LoginForm(request):
#     msg='dfdfdf'
#     return HttpResponse(msg)
