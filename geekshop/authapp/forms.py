from django.contrib.auth.forms import AuthenticationForm

from authapp.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args,**kwargs):
        super(UserLoginForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['placeholder']='Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите  пароль'
        for fields_name, fields in self.fields.items():
            fields.widget.attrs['class']= 'form-control py-4'

class UserRegisterForm(AuthenticationForm):
    pass
    # class Meta:
    #     model = User
    #     fields = ('username', 'password')