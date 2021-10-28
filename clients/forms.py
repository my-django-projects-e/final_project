from django.forms import ModelForm, Textarea, CheckboxInput
from .models import Client, Case


class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for form_field in self.visible_fields():
            form_field.field.widget.attrs['class'] = 'form-control w-75'
    class Meta:
        model = Client
        fields = '__all__'


class CaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CaseForm, self).__init__(*args, **kwargs)
        for form_field in self.visible_fields():
            if form_field.name != 'status':
                form_field.field.widget.attrs['class'] = 'form-control w-75'
            else:
                form_field.field.widget.attrs['class'] = 'form-check-input'
    class Meta:
        model = Case
        fields = '__all__'
        exclude = ['coordinator', 'client']
        widgets = {
            'notes': Textarea,
            'status': CheckboxInput
        }

