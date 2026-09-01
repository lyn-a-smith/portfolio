from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Your Name'})
        )
    email = forms.EmailField(
        max_length=50, widget=forms.EmailInput(attrs={'placeholder': 'Your Email'})
        )
    message = forms.CharField(
        max_length=500, widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 5})
        )