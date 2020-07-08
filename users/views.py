from django.shortcuts import render, redirect
from django.contrib import messages as m
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.models import User
from django.http import Http404



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            m.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
       
        if u_form.is_valid():
            u_form.save()
            m.success(request, f'Your account has been updated!')
            return redirect('profile_view', request.user)

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }

    return render(request, 'users/profile.html', context)

def profile_view(request, name):
    getUser = User.objects.get(username=name)
    getUserPost = getUser.post_set.all()
    context = {
        'user_profile': getUser,
        'posts': getUserPost
    }
    return render(request, 'users/profile_view.html', context=context)

