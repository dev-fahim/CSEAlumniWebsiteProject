from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.is_staff = True
            user.save()
            login(request, user)
            g = Group.objects.all().first()
            g.user_set.add(user)
            return redirect('admin:index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
