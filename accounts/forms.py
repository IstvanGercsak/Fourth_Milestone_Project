from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    """ Form to be used to log users in """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# UserCreationForm-ot orokli, igy ugy fog viselkedni az osztaly, mint amilyen parametert megkatp
#
class UserRegistrationForm(UserCreationForm):
    """ Form used to register a new user """
    # Ha csak simap password-ot adok meg akkor alapbol kiad validacios uzenetet
    # Ha password1-nek irom meg, akkor nincs predefined ellenorzo uzenet

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    username = forms.CharField(required=True)

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)

    # Creata a class into the class to create meta data of this class. Ezert Meta a neve
    # Itt leirhatoak egyeb tulajdonasgai
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    # FORM VALIDATION: DJANGO HANDLES IN THIS WAY;
    # the way django handles this is it takes a form and any form object that contains a cleaned
    # _field name method it will use that method to clean that field or
    # validate that field so clean underscore email will allow us to clean
    # the email field and it will expect us to return the email once we're done
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # ide nem kell a username, csak megmutatta, hogy van exclude. DE MI A FASZNAK...
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError("Email address must be unique!")

        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if not password1 or not password2:
            return ValidationError("Please confirm your password")
        if password1 != password2:
            return ValidationError("Password must match")

        return password2


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password'
        )


class EditPassword(PasswordChangeForm):
    """ """
