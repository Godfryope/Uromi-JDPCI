from django import forms
from .models import Message, Subscription

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control bg-light border-0',
                'placeholder': 'Your Name',
                'style': 'height: 55px;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-light border-0',
                'placeholder': 'Your Email',
                'style': 'height: 55px;'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control bg-light border-0 py-3',
                'placeholder': 'Message',
                'style': 'height: 150px;'
            }),
        }

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control border-primary rounded-pill w-100 py-3 ps-4 pe-5',
                'placeholder': 'Your email',
                'style': 'height: 55px;',
            }),
        }
