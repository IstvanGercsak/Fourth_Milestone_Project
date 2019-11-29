from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from accounts.forms import UserLoginForm, UserRegistrationForm, EditProfileForm, PasswordChangeForm


# Create your views here.

def index(request):
    return render(request, "index.html")


@login_required()
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect(reverse("index"))


def error_404(request):
    return render(request, '404.html')


def error_500(request):
    return render(request, '404.html')


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('view_feed'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('view_feed'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, "login.html", {"login_form": login_form})


def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse("index"))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse("index"))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()

    return render(request, "registration.html", {"registration_form": registration_form})


@login_required()
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "User details has changed successfully!")
            return redirect(reverse('profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit.html', args)


@login_required()
def user_profile(request):
    user_form = request.user
    return render(request, "profile.html", {"user_form": user_form})


@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('profile'))
        else:
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'change-password.html', args)
