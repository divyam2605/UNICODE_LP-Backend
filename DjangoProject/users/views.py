from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from .forms import UserRegisterForm
#from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(request.POST)
        print(form)
        if form.is_valid():
            print("The form is valid")
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created. Now you will be able to login!')
            return redirect('todolist-home')
    else:
        form = UserRegisterForm(request.POST)
    return render(request, 'register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'profile.html')