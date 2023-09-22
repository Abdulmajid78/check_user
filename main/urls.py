from django.urls import path
from .views import HomeView, ContactView, AboutView

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('about/', AboutView.as_view(), name='about'),

]