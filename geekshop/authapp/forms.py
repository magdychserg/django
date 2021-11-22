from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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

class UserRegisterForm(UserCreationForm):
    pass
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name', 'password1','password2')


    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите  email'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Введите повторно пароль'
        for fields_name, fields in self.fields.items():
            fields.widget.attrs['class'] = 'form-control py-4'