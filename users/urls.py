from django.urls import path
from . import views
app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    #
    # path('profile/', ProfileView.as_view(), name='account'),
    # path('logout/', logout_view, name='logout'),
    # path('login/', login_view, name='sign-in'),
    # # path('registration/', user_registration, name='sign-up'),
    # #####
    # path('register/', views.user_registration, name='sign-up'),
    # ###
    # path('profile/', ResetPasswordView.as_view(), name='reset-password')
]
