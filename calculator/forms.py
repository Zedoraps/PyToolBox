from django import forms


class CalculatorForm(forms.Form):
    reached_points = forms.IntegerField(label="Reached Points", min_value=0)
    max_points = forms.IntegerField(label="Max Points", min_value=1)
    reset = forms.BooleanField(label="Reset", initial=False, required=False)
