from django.urls import path
from .views import (CandidatesView, CandidateDetailsView, SignInView, SignUpView, FindJobView,
                    JobListView, JobDetailView, PostJobView, AccountView, ResumeView, ResetPasswordView)

app_name = 'users'

urlpatterns = [
    path('candidates/', CandidatesView.as_view(), name='candidate'),
    path('candidates/details/', CandidateDetailsView.as_view(), name='candidate-details'),
    path('find-job/', FindJobView.as_view(), name='find-job'),
    path('job-list/', JobListView.as_view(), name='job-list'),
    path('job-list/post', PostJobView.as_view(), name='post-job'),
    path('job-list/details/', JobDetailView.as_view(), name='job-detail'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('account/', AccountView.as_view(), name='account'),
    path('resume/', ResumeView.as_view(), name='resume'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),

]
