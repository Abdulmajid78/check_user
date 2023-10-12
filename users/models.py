from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _

######################

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    company_name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.username


##############


#
# CITY = (
#     ('Toshkent', 'Ташкент'),
#     ('Toshkent viloyati', 'Ташкентская область'),
#     ('Samarqand viloyati', 'Самаркандская область'),
#     ('Farg’ona viloyati', 'Ферганская область'),
#     ('Qashqadaryo viloyati', 'Кашкадарьинская область'),
#     ('Andijon viloyati', 'Андижанская область'),
#     ('Namangan viloyati', 'Наманганская область'),
#     ('Buxoro viloyati', 'Бухарская область'),
#     ('Qoraqalpog’iston Respublikasi', 'Республика Каракалпакстан'),
#     ('Xorazm viloyati', 'Хорезмская область'),
#     ('Jizzax viloyati', 'Джизакская область'),
#     ('Navoiy viloyati', 'Навоийская область'),
#     ('Sirdaryo viloyati', 'Сырдарьинская область')
# )
#
#
# class UserModel(AbstractUser):
#     username = models.CharField(max_length=50, unique=True)
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []
#
#     class Meta:
#         verbose_name = 'user'
#         verbose_name_plural = 'users'
#
#
class EmployeeModel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profiles', null=True, blank=True)
#
#     first_name = models.CharField(max_length=50, null=True)
#     last_name = models.CharField(max_length=50, null=True)
#     third_name = models.CharField(max_length=50, null=True, blank=True)
#
#     phone_number = models.CharField(max_length=17, null=True, blank=True)
#
#     born_city = models.CharField(max_length=50, choices=CITY, null=True, blank=True)
#     current_city = models.CharField(max_length=50, choices=CITY, null=True, blank=True)
#
#     # education
#     # school = models.ForeignKey(
#     #     SchoolModel,
#     #     on_delete=models.CASCADE,
#     #     null=True,
#     #     blank=True,
#     #     related_name='school'
#     # )
#
#     # collage = models.ForeignKey(
#     #     CollegeModel,
#     #     on_delete=models.CASCADE,
#     #     null=True,
#     #     blank=True,
#     #     related_name='college'
#     # )
#
#     # university = models.ForeignKey(
#     #     UniversityModel,
#     #     on_delete=models.CASCADE,
#     #     null=True,
#     #     blank=True,
#     #     related_name='university'
#     # )
#
#
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     is_applicant = models.BooleanField(default=False)
#     is_employer = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.first_name
#
#
#
#
#
#
#
# class SchoolModel(models.Model):
#     pass
#
#
# class CollegeModel(models.Model):
#     pass
#
#
# class UniversityModel(models.Model):
#     pass
