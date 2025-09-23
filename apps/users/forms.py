from django.contrib.auth.forms import UserCreationForm

from apps.users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    # class Meta(UserCreationForm.Meta):
        class Meta:
            model = CustomUser
            fields = ['last_name','first_name', 'email', 'password1', 'password2']

