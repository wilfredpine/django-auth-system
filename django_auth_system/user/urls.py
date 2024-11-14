from django.urls import path
from django.conf.urls import handler404
from . import views

handler404 = 'user.views.custom_404_view'

urlpatterns = [
    path('signup/', views.signup.as_view(), name='signup'),
    path('login/', views.sigin.as_view(), name='login'),
    path('logout/', views.signout, name='logout'),
    path('password_reset/', views.ForgotPasswordView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', views.ResetPasswordView.as_view(), name='password_reset_confirm'),
    path('verify/', views.verify.as_view(), name='verify'),
    path('verified/<uidb64>/<token>/', views.verified, name='verified'),
]