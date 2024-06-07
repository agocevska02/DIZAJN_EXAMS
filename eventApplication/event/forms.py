from django import forms

from event.models import Event


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
        field.label = ''
        self.fields['name'].widget.attrs['placeholder'] = 'Event Name'
        self.fields['date'].widget.attrs['placeholder'] = 'mm/dd/yyy'
        self.fields['time'].widget.attrs['placeholder'] = 'hh:mm:ss'
        self.fields['poster'].widget.attrs['placeholder'] = ''
        self.fields['bends'].widget.attrs['placeholder'] = 'Bends'

    class Meta:
        model = Event
        exclude = ('user', 'participants')
