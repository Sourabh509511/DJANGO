from django.urls import path
from . import views

urlpatterns= [
    path('',views.index),
    path('register/',views.register,name='register'),
    path('register/submit/',views.submit,name='submit'),
    path('accounts/login/',views.login),
    path('accounts/login/welcome',views.login_user)
]