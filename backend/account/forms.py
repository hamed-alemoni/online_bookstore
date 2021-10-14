from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField()
        if not user.is_superuser:
            self.fields['username'].disabled = True
            self.fields['email'].disabled = True

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
