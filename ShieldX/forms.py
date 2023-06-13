from .models import UserRelatives,CarRegistration
from django import forms

        # relative.userRelativeImage
class UserRelativeProfileForm(forms.ModelForm):
    class Meta:
        model = UserRelatives
        fields = ['userRelativeFirstName','userRelativeLastName','userRelativeEmail','userRelativeNumber','userRelativeImage']
        widgets = {
            'userRelativeFirstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'userRelativeLastName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'userRelativeEmail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'userRelativeNumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Phone number'}),
            # 'userRelativeImage': ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            # 'userRelativeNumber': forms.ImageField(attrs={'class': 'form-control', }),
        }


class CarRegistrationForm(forms.ModelForm):
    class Meta:
        model = CarRegistration
        fields = ['carHolderName','carModel','carMobileNumber','carMobileEmail']
        widgets = {
            'carHolderName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter car holder name'}),
            'carModel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your car model'}),
            'carMobileEmail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Registered Car Email'}),
            'carMobileNumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Registered Car Mobile Number'}),
        }