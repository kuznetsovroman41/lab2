from django import forms
from django.contrib.auth.forms import UserCreationForm
from ..models.custom_user import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    avatar = forms.ImageField(required=False)
    full_name = forms.CharField(max_length=150, required=False)
    info = forms.CharField(widget=forms.Textarea, required=False)
    phone = forms.CharField(max_length=20, required=False)
    gender = forms.ChoiceField(choices=CustomUser.gender_choices, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'avatar', 'password1', 'password2', 'full_name', 'info', 'phone', 'gender')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует.')
        return email

