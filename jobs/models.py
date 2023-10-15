from django.db import models
from users.models import EmployeeModel


class CommentModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    email = models.EmailField(verbose_name='email')
    phone = models.CharField(max_length=10, verbose_name='phone')
    comment = models.TextField(verbose_name='comment')
    employee = models.ForeignKey(EmployeeModel, on_delete=models.RESTRICT, related_name='comments', verbose_name='employee')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
