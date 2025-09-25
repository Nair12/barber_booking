from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from apps.users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    # class Meta(UserCreationForm.Meta):
        class Meta:
            model = CustomUser
            # fields = ['last_name','first_name','username','email','photo' ,'password1', 'password2']
            fields = ['last_name','first_name','username','email','password1', 'password2']


