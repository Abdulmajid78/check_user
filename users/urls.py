from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('register/individual/', views.register_individual, name='register'),
    path('register/company/', views.register_company, name='register-company'),
    path('update-company-profile/<int:pk>/', views.CompanyProfileUpdateView.as_view(), name='update-company-profile'),

    path('add_employee/', views.add_employee, name='add_employee'),
]
