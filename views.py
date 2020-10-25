from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# from django.db import models
# from voom_logs.models import User


def register(request):
    """ Register a new user. """
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('voom_logs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def profile(request):
    """ Show info on the user. """
    return render(request, 'users/you.html')
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
