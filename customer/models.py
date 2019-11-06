from django.db import models

# Create your models here.
from django.contrib.auth.models import User, BaseUserManager
from django.utils.crypto import get_random_string


class UsersManager(BaseUserManager):
    def create_administrator(self, username, first_name, last_name):
        customer = Customer(username=username,
                            first_name=first_name, last_name=last_name)
        password = get_random_string(length=6)
        customer.set_password(password)
        customer.is_staff = True
        customer.save()
        return customer


class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
