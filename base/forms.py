from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['fullname', 'phone', 'email', 'message']
        widgets = {
            'fullname': forms.TextInput(attrs={
                'placeholder': 'Username or Fullname',
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone Number',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email Address',
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Enter Your Message...',
                'class': 'form-control',
                'rows': 4
            }),
        }