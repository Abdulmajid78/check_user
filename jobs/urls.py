from django.urls import path

from . import views
from .views import (CandidatesView, EmployeeDetailView, FindEmployeeView, CompanyListView, CompanyDetailView, JobDetailView, PostJobView,
                    ResumeView, CommentCreateView)

app_name = 'jobs'

urlpatterns = [
    path('add_employee/', views.add_employee, name='add_employee'),
    path('find-employee/', FindEmployeeView.as_view(), name='find-employee'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),

    path('employee/<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),

    path('companies-list/', CompanyListView.as_view(), name='companies-list'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),

    path('candidates/', CandidatesView.as_view(), name='candidate'),
    path('job-list/post', PostJobView.as_view(), name='post-job'),
    path('job-list/details/', JobDetailView.as_view(), name='job-detail'),
    path('resume/', ResumeView.as_view(), name='resume'),

]

# path('<int:employee_id>/comment/', views.employee_comment, name='employee_comment'),
