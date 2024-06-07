from django import forms

from app.models import Reservation


class ReservationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            if field.name != 'id_photo':
                field.field.widget.attrs["class"] = "form-control"
            field.label = '' #da nemaat field label name
            self.fields['start_date'].widget.attrs['placeholder'] = 'mm/dd/yyy'
            self.fields['end_date'].widget.attrs['placeholder'] = 'mm/dd/yyy'
            self.fields['name_surname'].widget.attrs['placeholder'] = 'Name and Surname'
            self.fields['room'].widget.attrs['placeholder'] = ''

    class Meta:
        model = Reservation
        exclude = ['user', 'employer', 'isReserved', 'code']
