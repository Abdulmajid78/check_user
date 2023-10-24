from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _

######################

from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    address = models.TextField()
    is_individual = models.BooleanField(default=False)


class IndividualUser(CustomUser):
    is_individual = True


class CompanyUser(CustomUser):
    company_name = models.CharField(max_length=100, null=True, blank=True)
    is_individual = False


class CompanyProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    address = models.TextField()
    year_of_establishment = models.PositiveIntegerField()
    # Add other fields as needed


###################### down



class EmployeeModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='profiles', null=True, blank=True)
    #
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    third_name = models.CharField(max_length=50, null=True, blank=True)

    phone_number = models.CharField(max_length=17, null=True, blank=True)

    born_city = models.CharField(max_length=50, null=True, blank=True)
    current_city = models.CharField(max_length=50, null=True, blank=True)

    # about_me
    # expirience



    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_applicant = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

##################### up
