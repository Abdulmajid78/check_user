from django.db import models
from django.urls import reverse

import users.models
from users.models import CompanyUser


class CityModel(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Shahar'
        verbose_name_plural = 'Shaharlar'


class ExperienceModel(models.Model):
    title = models.CharField(max_length=49)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tajriba'
        verbose_name_plural = 'Tajribalar'


class EmployeeModel(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='profiles', null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    third_name = models.CharField(max_length=50, null=True, blank=True)

    phone_number = models.CharField(max_length=17, null=True, blank=True)

    born_date = models.DateField()

    born_city = models.ForeignKey(CityModel, on_delete=models.RESTRICT, related_name='born_city')
    current_city = models.ForeignKey(CityModel, on_delete=models.RESTRICT, related_name='current_city')

    about = models.TextField(null=True, blank=True)
    experience = models.ManyToManyField(ExperienceModel, null=True, blank=True, related_name='experience')

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_applicant = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("jobs:employee-detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Ishchi'
        verbose_name_plural = 'Ishchilar'
        ordering = ('-id',)


class CompanyModel(models.Model):
    user = models.OneToOneField(users.models.CompanyUser, on_delete=models.CASCADE, null=True, blank=True)

    company_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=24)
    address = models.TextField()
    description = models.TextField()
    site = models.CharField(max_length=255)
    is_individual = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Kompaniya'
        verbose_name_plural = 'Kompaniyalar'
        ordering = ('-id',)


class Comment(models.Model):
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    position = models.CharField(max_length=60)
    employ_from = models.DateField()
    employ_to = models.DateField()
    content = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Ish tajriba'
        verbose_name_plural = 'Ish tajribalar'
        ordering = ['created_at']

        indexes = [
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.employee}'

