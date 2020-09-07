from django.forms import ModelForm
from ..models.user import User


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ('user_name', 'mail_address', 'password', )