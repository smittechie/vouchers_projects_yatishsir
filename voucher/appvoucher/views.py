from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import   AuthenticationForm
from django.urls import reverse_lazy
from .forms import SignUpForm ,  LogInForm
from .models import Employee, Voucher
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import View
from django.http import HttpResponseRedirect


# Create your views here.
class Home(TemplateView):
    template_name = 'appvoucher/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['employee'] = Employee.objects.all()
        context['voucher'] = Voucher.objects.all()
        return context

    # extra_context = {'vouch': Voucher.objects.all()}            ##this is for extra context in data


class Voucher_Detail(DetailView):
    model = Voucher


def Employee_Detail(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        employee = None
    # context = {'employee': employee}
    # context = employee
    # print(context)
    return render(request, 'appvoucher/employee_detail.html', {'context': employee})


class Employeelist(TemplateView):
    template_name = 'appvoucher/employee_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Employeelist, self).get_context_data(*args, **kwargs)
        context['employee'] = Employee.objects.all()
        return context

class Voucherlist(TemplateView):
    template_name = 'appvoucher/voucher_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Voucherlist, self).get_context_data(*args, **kwargs)
        context['voucher'] = Voucher.objects.all()
        return context

# def signup_form(self,request):
#     data = SignUpForm()
#
#     return render(request, template_name='appvoucher/login.html')


class SignupForm(CreateView):
    template_name = 'appvoucher/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')


'''Trying user creation form '''


# class SignupView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'appvoucher/signup.html'


""" Login Form """
def login_user(request):
    if request.POST:
        form = LogInForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))

            if user is None:
                return render(request, "appvoucher/login.html")
            else:
                print(user)
                login(request, user)
                return redirect("home")
    context = {'form': LogInForm}
    return render(request, "appvoucher/login.html",context)





# class LoginView(View):
#
#
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