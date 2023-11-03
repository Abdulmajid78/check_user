from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('', include('django.contrib.auth.urls')),
    path('edit/', views.edit, name='edit'),

    path('dashboard/', views.dashboard, name='dashboard'),

]
#

# path('company-profile/', views.company_profile_view, name='company_profile'),

# # url-адреса смены пароля
# path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
# path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
#
# # url-адреса сброса пароля
# path('password-reset/',
#      auth_views.PasswordResetView.as_view(),
#      name='password_reset'),
# path('password-reset/done/',
#      auth_views.PasswordResetDoneView.as_view(),
#      name='password_reset_done'),
# path('password-reset/<uidb64>/<token>/',
#      auth_views.PasswordResetConfirmView.as_view(),
#      name='password_reset_confirm'),
# path('password-reset/complete/',
#      auth_views.PasswordResetCompleteView.as_view(),
#      name='password_reset_complete'),

# path('register/individual/', views.register_individual, name='register'),
# path('user-profile/', views.user_profile_view, name='user_profile'),  # пока обычные пользователи не
# path('update-company-profile/<int:pk>/', views.CompanyProfileUpdateView.as_view(), name='update-company-profile'),
# path('profile/', views.profile_view, name='profile'),
