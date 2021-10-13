from django import forms
from .models import User


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProfileForm, self).__init__(*args, **kwargs)
        if not user.is_superuser:
            self.fields['username'].disabled = True
            self.fields['email'].disabled = True

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
