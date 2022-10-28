from statistics import mode
from attr import field



from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ("email",)
        widgets = {
            "email": forms.TextInput(attrs={"class": "editContent", "placeholder":"Enter your email.."})
        }
        labels = {
            "email": ''
        }