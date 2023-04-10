from django import forms

from .models import Participant


class RegistrationForm(forms.Form):
    email = forms.EmailField(label="Enter Email")
    # class Meta:
    #     model = Participant
    #     fields = "__all__"
