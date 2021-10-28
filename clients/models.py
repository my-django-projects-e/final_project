from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Client(models.Model):
    policy_num = models.CharField(max_length=20, null=True, blank=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    birthday_date = models.DateField(null=True, blank=True)
    policy_start_date = models.DateField(null=True, blank=True)
    policy_end_date = models.DateField(null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.full_name


class Case(models.Model):
    num_case = models.IntegerField(null=True)
    case_start_date = models.DateField(null=True)
    case_end_date = models.DateField(null=True)
    status = models.BooleanField(null=True)
    client = models.ForeignKey('clients.Client', null=True, on_delete=models.CASCADE)
    coordinator = models.ForeignKey('account.Employee', null=True, on_delete=models.SET_NULL)
    notes = models.TextField(null=True)

    def __str__(self):
        return f'Страховой случай {self.num_case} клиента {self.client.full_name}'
