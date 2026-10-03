from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app1.models import *
from django.core.mail import send_mail

def main(request):
    return render(request, 'main.html')


def signup(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(
                request,
                'main.html',
                {'error': 'Passwords do not match'}
            )

        if User.objects.filter(username=username).exists():
            return render(
                request,
                'main.html',
                {'error': 'Username already exists'}
            )

        if User.objects.filter(email=email).exists():
            return render(
                request,
                'main.html',
                {'error': 'Email already exists'}
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('main')

    return redirect('main')


def login_user(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

        else:

            return render(
                request,
                'main.html',
                {'error': 'Invalid username or password'}
            )

    return redirect('main')


def logout_user(request):

    logout(request)

    return redirect('main')


@login_required
def home(request):

    projects = Project.objects.all()

    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            subject,
            f"""
Name: {name}
Email: {email}

Message:
{message}
""",
            'vigneshvicky24092005@gmail.com',
            ['vigneshvicky24092005@gmail.com'],
            fail_silently=False,
        )

    return render(
        request,
        'home.html',
        {'projects': projects}
    )
