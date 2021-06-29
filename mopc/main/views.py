from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView    

# Create your views here.

class MainLogin(LoginView):
    template_name = 'main/mainloginview.html'

def main(request):
    return render(request, 'main/main.html')

def about(request):
    return render(request, 'main/about.html')

def signup(request):
    if request.user.is_authenticated:
        messages.error(request, 'You are already signed up and logged in!!')
        return redirect('main')

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            user = authenticate(request, username=new_user.username, password=form.cleaned_data['password1'])
            if user:
                login(request, user)
            messages.success(request, 'Account created successfully')
            return redirect('main')
        else:
            messages.error(request, 'there was a problem with your signup data, please try again')
    return render(request, 'main/signup.html', {'form':form})