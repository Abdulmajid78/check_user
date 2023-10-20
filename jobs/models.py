from django.db import models
from users.models import EmployeeModel

from django.contrib.auth.models import User
from users.models import CustomUser, EmployeeModel

from users.models import EmployeeModel, CompanyUser


class Comment(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=40)
    employ_from = models.DateField()
    employ_to = models.DateField()

    content = models.TextField()
    post = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)