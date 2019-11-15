from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm


# Create your views here.

def index(request):
    """" Return the index.html file """
    return render(request, "index.html")


# Minden esemenyt ez a fuggveny fog megelozni, azaz ha be akarunk lepni, akkor ez a dekaorator
# fogja intezni azt, hogy elobb jelentkezzunk be ne pedig hibat kpajunk
# Mindenkepp lepjunk be hogy elerheto legyen a kilepes opcio
@login_required()
def logout(request):
    """" Log the user out """
    # Request contains the user object
    auth.logout(request)
    # Reverse allows us to pass the name of a URLs instead of a name of a view
    messages.success(request, "You have successfully logged out")
    return redirect(reverse("index"))


def login(request):
    """ Return a login page (this is a dock string) """
    # Ha megint a login oldalra akarunk menni, akkor nem a login oldalra erkezunk,
    # hanem ha mar autentikaltuk magunkat, be azonnal
    # megyunk a Home(be vagyunk jelentkezve) oldalra
    # Ha ez a kod nincs, akkor a login oldal jelenik meg
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        # Ha jon vissza adat akkor meg nezni, hogy valid e
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            messages.success(request, "You have successfully logged in!")

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        # Maskulonben letrehozi egy ures
        login_form = UserLoginForm()
    return render(request, "login.html", {"login_form": login_form})


def registration(request):
    """ Render the registration page"""
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


def edit_profile(request):
    """ Edit user profile """
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit.html', args)


def user_profile(request):
    """ The user's profile page """
    user_form = request.user
    return render(request, "profile.html", {"user_form": user_form})
