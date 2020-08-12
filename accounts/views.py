from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import LoginForm, UserRegistrationForm
from accounts.models import Profile
from links.models import Link


def public_profile(request, uname):
    # TODO check if uname exists
    user = User.objects.filter(username__exact=uname)
    if user:
        # TODO action.create(profile_viewed)
        # TODO page_viewed++
        user = User.objects.filter(username__exact=uname)
        # username = request.GET.get(uname)
        links = Link.objects.filter(user__username=uname)
        context = {
            'user': user,
            'uname': uname,
            'links': links
        }
        return render(request, 'accounts/public_profile.html', context)
    else:
        return HttpResponse('User Not found')


def register(request):
    if request.user.is_authenticated:
        return  redirect('index')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = form.save(commit=False)
            # Set the chosen password
            new_user.set_password(form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            # create_action(new_user, 'has created an account')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return  redirect('index')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = auth.authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('link_list')
                    # return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')
