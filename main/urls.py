from django.urls import path
from .views import HomeView, ContactView, CandidatesView, CandidateDetailsView

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('candidates/', CandidatesView.as_view(), name='candidate'),
    path('candidates-details/', CandidateDetailsView.as_view(), name='candidate-details'),
]