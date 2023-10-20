from django.urls import path
from .views import (CandidatesView, EmployeeDetailsView, FindEmployeeView, JobListView, JobDetailView, PostJobView, ResumeView)

app_name = 'jobs'

urlpatterns = [
    path('find-employee/', FindEmployeeView.as_view(), name='find-employee'),
    path('employee/<int:pk>/', EmployeeDetailsView.as_view(), name='employee-detail'),

    path('candidates/', CandidatesView.as_view(), name='candidate'),
    path('job-list/', JobListView.as_view(), name='job-list'),
    path('job-list/post', PostJobView.as_view(), name='post-job'),
    path('job-list/details/', JobDetailView.as_view(), name='job-detail'),
    path('resume/', ResumeView.as_view(), name='resume'),

]
