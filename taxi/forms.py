from django import forms
# from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from taxi.models import Driver, Car
from taxi.validators import validate_license_number


class CarCreateForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=Driver.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    class Meta:
        model = Car
        fields = "__all__"


class DriverCreateForm(UserCreationForm):
    license_number = forms.CharField(
        required=False,
        validators=[validate_license_number],
        help_text="Must match the following pattern: ABC12345",
    )

    class Meta:
        model = Driver
        fields = ("username", "first_name", "last_name", "license_number", )


class DriverLicenseUpdateForm(forms.ModelForm):
    license_number = forms.CharField(
        validators=[validate_license_number],
        help_text="Must match the following pattern: ABC12345",
    )

    class Meta:
        model = Driver
        fields = ("license_number", )
