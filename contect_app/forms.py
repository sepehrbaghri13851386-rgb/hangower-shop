from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control mt-1', 'placeholder': 'Message', 'rows': 8}),
        }