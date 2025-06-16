from django import forms 
from .models import Blog

class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog 
        fields = ['title','image','text']
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'text': forms.TextInput(attrs={'class': 'form-control'}),
    }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'accept': 'image/*'
        })

