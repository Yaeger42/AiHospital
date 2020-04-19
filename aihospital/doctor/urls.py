"""Doctors urls"""
# Django imports
from django.urls import path

# View
from doctor import views

urlpatterns = [
    # Management

    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),

    path(
        route='login',
        view=views.LoginView.as_view(),
        name='login'
    )
]
