from django import forms

from authapp.forms import UserRegisterForm
from authapp.models import User


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)

        for fields_name, fields in self.fields.items():
            fields.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'
