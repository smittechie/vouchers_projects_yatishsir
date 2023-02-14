from django.shortcuts import render
from django.views.generic import TemplateView ,ListView , CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm, LogInForm
from .models import Employee, Voucher
from django.http import HttpResponse


# Create your views here.
class Home(TemplateView):
    template_name = 'registration/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['emp'] = Employee.objects.all()
        context['vouch'] = Voucher.objects.all()
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
    return render(request, 'registration/employee.html', {'context': employee})


# def signup_form(self,request):
#     data = SignUpForm()
#
#     return render(request, template_name='registration/login.html')


# class SignupForm(TemplateView,ListView):
#     template_name = 'registration/signup.html'
#     form_class  = SignUpForm()
#     context_object_name = 'form'

'''Trying user creatoion form '''
class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class LoginForm(TemplateView):
    template_name = 'registration/login.html'
    form_class  = LogInForm()