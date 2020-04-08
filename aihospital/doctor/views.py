"""Doctors views"""
# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth import views as auth_views

# Models imports
from django.contrib.auth.models import User
from doctor.models import Profile

# Forms import
from doctor.forms import SignupForm


class SignupView(FormView):
    """Doctors form view"""
    template_name = 'doctor/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('doctor:login')

    def form_valid(self, form):
        """Save form Data"""
        form.save()
        return super().form_valid(form)

class LoginView(auth_views.LoginView):
    """Login view inherits from auth views"""
    template_name = 'doctor/login.html'
