from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import DetailView, UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileForm
from .models import Profile
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # Создаем профиль для нового пользователя
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # Создаем профиль, если его нет
            if not Profile.objects.filter(user=user).exists():
                Profile.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'users/profile.html'

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        return self.request.user.profile

@login_required
@require_POST
def profile_image_upload(request):
    profile = request.user.profile
    form = ProfileForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your profile image was successfully updated!')
    return redirect('profile', pk=request.user.pk)

@login_required
def profile_update_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile', pk=request.user.pk)
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def profile_view(request, pk):
    profile, created = Profile.objects.get_or_create(user=request.user)
    user_form = CustomUserChangeForm(instance=request.user)
    profile_form = ProfileForm(instance=profile)
    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})
