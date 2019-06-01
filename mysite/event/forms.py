from django import forms
from .models import Event, Participant


class CreateEvent(forms.ModelForm):   

    name = forms.CharField(
        label='Имя',
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

    class Meta:
        model = Event
        fields = ('name', 'text', 'photo')

class ParticipantForm(forms.ModelForm):

    text = forms.TextInput(
    )
    
    photo = forms.ImageField(
        label='Фотография',
        help_text='',
        required=True,
    )

    class Meta:
        model = Participant
        fields = ('text', 'photo')