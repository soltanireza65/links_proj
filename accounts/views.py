from django.contrib import messages, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import LoginForm, UserRegistrationForm, ProfileEditForm, RegForm
from accounts.models import Profile
from links.models import Link


def public_profile(request, uname):
    # TODO check if uname exists
    user = User.objects.filter(username__exact=uname).get()
    # links = Link.objects.filter(user=request.user)
    if user:
        # TODO action.create(profile_viewed)
        # TODO page_viewed++
        # user = User.objects.filter(username__exact=uname).get()
        # profile = Profile.objects.filter(user=user).get()
        # username = request.GET.get(uname)
        links = Link.objects.filter(user__username=uname).filter(is_active=True)
        context = {
            'user': user,
            'section': 'profile',
            # 'profile': profile,
            'uname': uname,
            'links': links,
            'instagram_url': user.profile.instagram_url,
            'youtube_url': user.profile.youtube_url,
            'twitter_url': user.profile.twitter_url,
            'facebook_url': user.profile.facebook_url,
        }
        return render(request, 'accounts/public_profile.html', context)
    else:
        return HttpResponse('User Not found')


def profile_edit(request):
    user = request.user
    form = ProfileEditForm(instance=request.user.profile)
    # profile = Profile.objects.filter(user=user).get()

    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('public_profile', request.user.username)
        else:
            messages.error(request, 'Failed to Update')
            return redirect('profile_edit')

    context = {
        'form': form,
        'user': user,
        'section': 'edit',
        'profile_addr': 'http://127.0.0.1:8000/profile/' + user.username,
    }
    return render(request, 'accounts/profile_edit.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('link_list')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        # form = UserCreationForm(request.POST)

        if form.is_valid():

            new_user = form.save(commit=False)

            new_user.set_password(form.cleaned_data['password1'])

            new_user.save()

            Profile.objects.create(user=new_user)

            return redirect('login')
    else:
        form = UserRegistrationForm()
        # form = UserCreationForm()
        # form = RegForm()
    return render(request, 'accounts/register.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('link_list')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = auth.authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'You Are Logged In')
                    return redirect('link_list')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    # messages.success(request, 'You are now logged out')
    return redirect('index')
