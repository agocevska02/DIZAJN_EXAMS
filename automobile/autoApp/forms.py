from django import forms

from autoApp.models import Fix


class FixForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FixForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Fix
        exclude = ['user', ]
