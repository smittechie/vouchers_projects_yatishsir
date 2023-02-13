from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Employee, Voucher


# Create your views here.
class Home(TemplateView):
    template_name = 'registration/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['emp'] = Employee.objects.all()
        context['vouch'] = Voucher.objects.all()
        return context

    # extra_context = {'vouch': Voucher.objects.all()}            ##this is for extra context in data

# def Employee_Detail(DetailView):
#     model = Employee



def Employee_Detail(request, id):
    try:
        employee = Employee.objects.filter(id=id)
    except Employee.DoesNotExist:
        employee = None
    context = {'employee': employee}
    return render(request, 'registration/employee.html', context)
