from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

from config import settings


class CompanyUser(AbstractUser):
    company_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=24)
    address = models.TextField()
    description = models.TextField()
    is_individual = models.BooleanField(default=False)

    @property
    def is_companyuser(self):
        return isinstance(self, CompanyUser)

    class Meta:
        verbose_name = 'Kompanya'
        verbose_name_plural = 'Kompaniyalar'


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    about = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100)
    address = models.TextField()
    year_of_establishment = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'

    class Meta:
        verbose_name = 'Kompaniya profili'
        verbose_name_plural = 'Kompaniya profillari'

#
# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The Username field must be set')
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(username, password, **extra_fields)
#
#     class Meta:
#         verbose_name = 'CustomUserManager user'
#         verbose_name_plural = 'CustomUserManager users'
#

# class IndividualUser(CustomUser):
#     is_individual = True
#
#     class Meta:
#         verbose_name = 'Individual user'
#         verbose_name_plural = 'Company users'


# class UserProfile(models.Model):
#     user = models.OneToOneField(IndividualUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)


#
# class ProfileModel(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     company_name = models.CharField(max_length=244, null=True, blank=True)
#     about = models.TextField(null=True, blank=True)
#     address = models.TextField()
#     year_of_establishment = models.PositiveIntegerField()
#
#     def __str__(self):
#         return self.user.first_name
#
#     class Meta:
#         verbose_name = 'Company profile'
#         verbose_name_plural = 'Company profiles'
