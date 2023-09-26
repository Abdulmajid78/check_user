from django.urls import path
from .views import HomeView, ContactView, AboutView, BlogView, BlogDetailsView

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('about/', AboutView.as_view(), name='about'),
    path('blogs/', BlogView.as_view(), name='blog'),
    path('blog-details/', BlogDetailsView.as_view(), name='blog-details'),

]