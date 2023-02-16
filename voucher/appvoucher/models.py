from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password           ## make password in hash

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


# class Employee(models.Model):
#     name = models.CharField(max_length=40)
#     voucher = models.ManyToManyField(Voucher, related_name='vouchers')
#
#     def __str__(self):
#         return self.name


from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# class MyUserManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         """
#         Creates and saves a User with the given email, and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         user = self.model(
#             email=self.normalize_email(email),
#             # username = username
#         )
#         user.username = username
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, username, password=None):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#             username=username
#         )
#         user.is_staff=True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user


class Employee(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    # objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name ='Employee'