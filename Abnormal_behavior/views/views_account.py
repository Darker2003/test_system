from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import User_Management
import secrets
import string
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User
import random
import string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import authenticate, login
from django.conf import settings

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        random_string_length = 8

        if password == password2:
            # Check if username or email already exists
            if User_Management.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect('register')
            elif User_Management.objects.filter(mail=email).exists():
                messages.error(request, "Email already exists")
                return redirect('register')
            else:
                # Create new user
                new_user = User_Management(
                    username=username,
                    upassword=password,
                    mail=email,
                    phone=phone,
                    remainday=0,  # Example default value
                    ucode=''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(random_string_length)),  # Example default value
                    # utype is not specified here, so it will take the default value 'normal'
                )
                new_user.save()
                messages.success(request, "Your account has been created successfully")
                return redirect('login')  # Redirect to login page after registration
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')

    return render(request, 'Account/register.html')  # Render the registration page if not a POST request
def login(request):
    if 'user_name' in request.session:
        # User is logged in, render the course page
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        try:
            user = User_Management.objects.get(username=username, upassword=password)
            request.session['user_name'] = user.username  # Set a session variable
            request.session['utype'] = user.utype
            request.session['remainday'] = user.remainday
            # print("User Type:", request.session.get('utype'))
            # print("Remain Days:", request.session.get('remainday'))
            return redirect('home')
        except User_Management.DoesNotExist:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, "Account/login.html")

def changepassword(request):
    if 'user_name' not in request.session:
        # Redirect to login if the user is not logged in
        return redirect('login')

    if request.method == "POST":
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        try:
            user = User_Management.objects.get(username=request.session['user_name'])

            if user.upassword == current_password:
                if new_password == confirm_password:
                    # Update the password
                    user.upassword = new_password
                    user.save()
                    messages.success(request, "Password changed successfully.")
                    return redirect('changepassword')
                else:
                    messages.error(request, "New passwords do not match.")
            else:
                messages.error(request, "Current password is incorrect.")
        except User_Management.DoesNotExist:
            messages.error(request, "User not found.")

    return render(request, "Account/changepassword.html")

def logout(request):
    try:
        # Clear the session
        request.session.clear()
        messages.info(request, "You have been logged out successfully.")
    except KeyError:
        pass  # No session was found, which means user was not logged in
    # Redirect to the homepage or login page after logout
    return redirect('login')


def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        try:
            user = User_Management.objects.get(username=username, mail=email)
            print(user.ucode)
            token = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
            request.session['token'] = token
            request.session['username'] = user.username
            request.session['mail'] = user.mail
            send_password_reset_email(user,token)
            messages.success(request, "Password reset instructions sent to your email.")
        except User_Management.DoesNotExist:
            messages.error(request, "User with this username/email does not exist.")
        return redirect('login')
    return render(request, 'Account/forgot_password.html')


def send_password_reset_email(user,token):
    # Implement logic to send email with password reset link containing the token
    domain = '127.0.0.1:8000'
    
    reset_link = f"https://{domain}/reset-password/{user.username}/{token}/"
    # Send email with reset_link to user.email using Django's email system
    # Example:
    send_mail(
        'Password Reset',
        f'Please use the following link to reset your password: {reset_link}',
        'settings.EMAIL_HOST_USER',
        [user.mail],
        fail_silently=False,
    )

def reset_password(request, username, token):
    print("Reset password function called")  # Add this print statement for debugging
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        try:
            print("Inside try block")  # Add this print statement to test the try block
            user = User_Management.objects.get(username=username)
            print("Inside try block2")
            # Check if the token is valid (you might want to store the token in the database)
            if request.session.get('token') == token:
                # Reset the password and redirect to login page
                user.upassword = new_password
                user.save()
                print("Success")
                messages.success(request, 'Your password has been reset successfully. Please log in.')
                return redirect('login')
            else:
                print("invalid toekn")
                messages.error(request, 'Invalid token.')
        except User_Management.DoesNotExist:
            print("user not found")
            messages.error(request, 'User does not exist.')
    # Render the password reset form
    return render(request, 'Account/reset_password.html')

