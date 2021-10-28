from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Employee


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# форма для настроек пользователя
class EmployeeSettingsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmployeeSettingsForm, self).__init__(*args, **kwargs)
        for form_field in self.visible_fields():
            form_field.field.widget.attrs['class'] = 'form-control w-75'

    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['user', 'position', 'salary', 'date_created']

