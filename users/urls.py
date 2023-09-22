from django.urls import path
from .views import CandidatesView, CandidateDetailsView, SignInView, SignUpView

app_name = 'users'

urlpatterns = [
    path('candidates/', CandidatesView.as_view(), name='candidate'),
    path('candidates-details/', CandidateDetailsView.as_view(), name='candidate-details'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),

]
