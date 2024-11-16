from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm

# Define your views here
def home(request):
    return render(request, '1.html')

def comments(request):
    return render(request, '12.html')

def cart(request):
    return render(request, '6.html')

def notifications(request):
    return render(request, '13.html')

def profile(request):
    return render(request, '8.html')

def showroom_near_me(request):
    return render(request, '3.html')

def need_repair(request):
    return render(request, '2.html')

def details_view(request):
    return render(request, '4.html')

def terms_of_use(request):
    return render(request, '8.html')

def signup(request):
    return render(request, '8.html')

def place_order(request):
    return render(request, '7.html')

def checkoutbtn(request):
    return render(request, '10.html')

def checkout(request):
    return render(request, '11.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.contact = form.cleaned_data.get('contact')
            user.choose = form.cleaned_data.get('choose')
            user.save()
            auth_login(request, user)  # Use auth_login to log the user in immediately
            messages.success(request, f'Account created for {user.username}!')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, '8.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')  # Redirect to home after login
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')  # Redirect to login if authentication fails

    return render(request, '9.html')  # Render the login page if it's a GET request

@login_required
def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')
