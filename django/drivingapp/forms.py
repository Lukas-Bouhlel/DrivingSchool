from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class PlanningForm(forms.Form):
    date = forms.DateField(label="date", widget=DateInput)
    heure = forms.TimeField(label="heure", widget=TimeInput)
    lieu = forms.CharField(label="lieu", max_length=100)

class MyModelForm(forms.ModelForm):
    class Meta:
        widgets = {
            'date': DateInput(),
            'time': TimeInput()
        }
