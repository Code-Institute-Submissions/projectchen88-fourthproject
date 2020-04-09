from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required    
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))
    

def login(request):
    """Returns the login page"""
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST) # populate the form from what the user has keyed in
        if login_form.is_valid():
            # attempt to check the username and password is valid
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            messages.success(request, "You have successfully logged in")
            if user:
                # log in the user
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Invalid username or password")
                return render(request, 'login.html', {
                  'form':login_form
                })

    else:
        login_form = UserLoginForm()
        return render(request, 'login.html', {
            'form':login_form
        })

@login_required        
def profile(request):
    return render(request, 'profile.html')


def register(request):
    return render(request, 'register.html')
