from django.urls import path
from . import views
urlpatterns=[
    path('',views.login),
    path('ForgotPassword',views.forgotPassword),
    path('Signup',views.signup),
    path('user',views.logged),
]