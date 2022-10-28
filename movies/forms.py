from django import forms
from .models import Rewiews, Rating, RatingStar

class ContactForm(forms.Form):
    subject = forms.CharField(label = 'Topic', widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(label = 'Text', widget=forms.TextInput(attrs={'class':'form-control', "rows":5}))




class ReviewForm(forms.ModelForm):

    class Meta:
        model = Rewiews

        fields = ("name","email", "text")

class RatingForm(forms.ModelForm):

    star  = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None 
    )
    class Meta:
        model = Rating
        fields = ("star",)
