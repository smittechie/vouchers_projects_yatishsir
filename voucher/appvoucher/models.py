from django.db import models


#
#
# # Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Voucher(models.Model):
    name = models.CharField(max_length=40, default='DEFAULT VALUE')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=40)
    voucher_employee_have = models.IntegerField(max_length=20)
    voucher = models.ManyToManyField(Voucher, related_name='employee')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
