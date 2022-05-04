from django import forms


class PasswordForm(forms.Form):
    length = forms.IntegerField(label="Length for the password", max_value=50, min_value=5, initial=16)
    special_chars = forms.BooleanField(label="Include special chars?", initial=True, required=False)
