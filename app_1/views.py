from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserEmailForm, ProfileForm
from django.shortcuts import render, redirect

def home_view(request):
    return render(request, 'app_1/home.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.email = form.cleaned_data['email']
            user.profile.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'app_1/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'app_1/login.html', {'form': form})

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return render(request, 'app_1/logged_out.html')


@login_required
def dashboard_view(request):
    return render(request, 'app_1/dashboard.html', {'profile': request.user.profile})



@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        user_form = UserEmailForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('dashboard')
    else:
        user_form = UserEmailForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'app_1/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })