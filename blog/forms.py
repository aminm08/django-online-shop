from django import forms

from .models import BlogPost


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'short_description', 'text', 'cover', 'status']
        widgets = {
            'short_description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            
        }
