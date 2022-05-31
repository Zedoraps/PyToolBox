from django import forms


class NoteCalculator(forms.Form):
    max_points = forms.IntegerField(label='Max Points', max_value=10000, min_value=1, initial=100)
    reached_points = forms.IntegerField(label='Reached Points', max_value=10000, min_value=0)


class DiceForm(forms.Form):
    max_number = forms.IntegerField(label="Highest possible Number", min_value=2, max_value=10000, initial=6)


class TippingForm(forms.Form):
    input = forms.CharField(widget=forms.Textarea, required=True)


class PasswordGeneratorForm(forms.Form):
    length = forms.IntegerField(label='Length', max_value=10000, min_value=1, initial=16)
    special_chars = forms.BooleanField(label="Special Chars", initial=True)
