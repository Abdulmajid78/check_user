from django.urls import path
from .views import SignInView, SignUpView, ResetPasswordView, AccountView

app_name = 'users'

urlpatterns = [

    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('account/', AccountView.as_view(), name='account'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),

]
