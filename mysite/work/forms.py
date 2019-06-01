from django import forms
from .models import Work


class CreateWork(forms.ModelForm):   

    name = forms.CharField(
        label='Название',
        help_text='',
        required=True,
        max_length=50,
    )

    text = forms.TextInput(
    )

    photo = forms.ImageField(
        label='Фотография',
        help_text='',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super(CreateWork, self).__init__(*args, **kwargs)
        self.fields['text'].label = 'Описание'

    class Meta:
        model = Work
        fields = ('name', 'text', 'photo')
