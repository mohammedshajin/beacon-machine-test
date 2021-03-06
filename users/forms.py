from django.forms import ModelForm
from django. contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password']
        labels = {
            'first_name': 'Name',
            'email': 'Email'
        }