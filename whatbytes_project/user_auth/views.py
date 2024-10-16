from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
import logging

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  
    else:
        form = AuthenticationForm()
    return render(request, 'user_auth/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
        else:
            messages.error(request, "Error in registration. Please check your input.")
    else:
        form = UserCreationForm()
    return render(request, 'user_auth/signup.html', {'form': form})

# logger = logging.getLogger(__name__)

# def forgot_password_view(request):
#     if request.method == 'POST':
#         form = PasswordResetForm(request.POST)
#         if form.is_valid():
#             form.save(request=request)
#             logger.info("Password reset email sent to %s", form.cleaned_data['email'])
#             messages.success(request, "We've emailed you instructions for resetting your password.")
#             return redirect('password_reset_done')
#     else:
#         form = PasswordResetForm()
#     return render(request, 'user_auth/forgot_password.html', {'form': form})

def forgot_password_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            messages.success(request, "We've emailed you instructions for resetting your password.")
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'user_auth/forgot_password.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'user_auth/dashboard.html')

@login_required
def profile_view(request):
    return render(request, 'user_auth/profile.html')

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, "Your password was successfully updated!")
            return redirect('dashboard')
        else:
            messages.error(request, "Error updating your password. Please check your input.")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'user_auth/change_password.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')
