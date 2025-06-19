from django import forms
from .models import CMSModel

class CMSHomeSec1Form(forms.ModelForm):
    class Meta:
        model = CMSModel
        fields = ['page_name','section_name','title','sub_title','button_text_1','button_url_1','button_text_2','button_url_2','card_1_title','card_1_description','card_1_icon','card_2_title','card_2_description','card_2_icon','media_1']

        widgets = {
            'page_name': forms.TextInput(attrs={'class': 'form-control'}),
            'section_name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_title': forms.TextInput(attrs={'class': 'form-control'}),
            'button_text_1': forms.TextInput(attrs={'class': 'form-control'}),
            'button_url_1': forms.TextInput(attrs={'class': 'form-control'}),
            'button_text_2': forms.TextInput(attrs={'class': 'form-control'}),
            'button_url_2': forms.TextInput(attrs={'class': 'form-control'}),
            'card_1_title': forms.TextInput(attrs={'class': 'form-control'}),
            'card_1_description': forms.TextInput(attrs={'class': 'form-control'}),
            'card_1_icon': forms.TextInput(attrs={'class': 'form-control'}),
            'card_2_title': forms.TextInput(attrs={'class': 'form-control'}),
            'card_2_description': forms.TextInput(attrs={'class': 'form-control'}),
            'card_2_icon': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['media_1'].widget.attrs.update({
            'class': 'form-control',
            'accept': 'image/*'
        })


class CMSHomeSec2Form(forms.ModelForm):
    class Meta: 
        model = CMSModel
        fields = ['page_name','section_name','title','sub_title','button_text_1','button_url_1','button_text_2','button_url_2','card_1_title','card_1_description','card_1_icon','card_2_title','card_2_description','card_2_icon','media_2']

        widgets = {
            'page_name': forms.TextInput(attrs={'class': 'form-control'}),
            'section_name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_title': forms.TextInput(attrs={'class': 'form-control'}),
            'button_text_1': forms.TextInput(attrs={'class': 'form-control'}),
            'button_url_1': forms.TextInput(attrs={'class': 'form-control'}),
            'button_text_2': forms.TextInput(attrs={'class': 'form-control'}),
            'button_url_2': forms.TextInput(attrs={'class': 'form-control'}),
            'card_1_title': forms.TextInput(attrs={'class': 'form-control'}),
            'card_1_description': forms.TextInput(attrs={'class': 'form-control'}),
            'card_1_icon': forms.TextInput(attrs={'class': 'form-control'}),
            'card_2_title': forms.TextInput(attrs={'class': 'form-control'}),
            'card_2_description': forms.TextInput(attrs={'class': 'form-control'}),
            'card_2_icon': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['media_2'].widget.attrs.update({
            'class': 'form-control',
            'accept': 'image/*'
        })

class CMSHomeSec3Form(forms.ModelForm):
    class Meta:
        model = CMSModel
        fields = ['page_name','section_name','title','sub_title']
        widgets = {
            'page_name': forms.TextInput(attrs={'class': 'form-control'}),
            'section_name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_title': forms.TextInput(attrs={'class': 'form-control'}),
        }

    
class CMSHomeSec4Form(forms.ModelForm):
    class Meta:
        model = CMSModel
        fields = ['page_name','section_name','title','sub_title','icon_1','icon_2','icon_3','card_1_title','card_1_description','card_1_icon','media_3']
        widgets = {
            'page_name': forms.TextInput(attrs={'class': 'form-control'}),
            'section_name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_title': forms.TextInput(attrs={'class': 'form-control'}),
            'icon_1': forms.TextInput(attrs={'class': 'form-control'}),
            'icon_2': forms.TextInput(attrs={'class': 'form-control'}),
            'icon_3': forms.TextInput(attrs={'class': 'form-control'}),
            'card_1_title': forms.TextInput(attrs={'class': 'form-control'}),
            'card_1_description': forms.TextInput(attrs={'class': 'form-control'}),
            'card_1_icon': forms.TextInput(attrs={'class': 'form-control'}),  
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['media_3'].widget.attrs.update({
            'class': 'form-control',
            'accept': 'image/*'
        })

class CMSHomeSec5Form(forms.ModelForm):
    class Meta:
        model = CMSModel
        fields = ['page_name','section_name','title','sub_title','button_text_1','button_url_1','card_1_title','card_1_description','card_1_icon','card_2_title','card_2_description','card_2_icon','card_3_title','card_3_description','card_3_icon']
        widgets = {
            'page_name': forms.TextInput(attrs={'class': 'form-control'}),
            'section_name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_title': forms.TextInput(attrs={'class': 'form-control'}),
            'button_text_1': forms.TextInput(attrs={'class': 'form-control'}),
            'button_url_1': forms.TextInput(attrs={'class': 'form-control'}),
            'card_1_title': forms.TextInput(attrs={'class': 'form-control'}),
            'card_1_description': forms.TextInput(attrs={'class': 'form-control'}),
            'card_1_icon': forms.TextInput(attrs={'class': 'form-control'}),
            'card_2_title': forms.TextInput(attrs={'class': 'form-control'}),
            'card_2_description': forms.TextInput(attrs={'class': 'form-control'}),
            'card_2_icon': forms.TextInput(attrs={'class': 'form-control'}),
            'card_3_title': forms.TextInput(attrs={'class': 'form-control'}),
            'card_3_description': forms.TextInput(attrs={'class': 'form-control'}),
            'card_3_icon': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
class CMSAboutSec(forms.ModelForm):
    class Meta:
        model = CMSModel
        fields = ['page_name','section_name','header_title','title','sub_title','media_1','media_2','short_description','short_description_2','description','content_block_1','media_3','content_block_2','content_block_3']
        widgets = {
            'page_name': forms.TextInput(attrs={'class': 'form-control'}),
            'section_name': forms.TextInput(attrs={'class': 'form-control'}),
            'header_title': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_title': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description_2': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'content_block_1': forms.TextInput(attrs={'class': 'form-control'}),
            'content_block_2': forms.TextInput(attrs={'class': 'form-control'}),
            'content_block_3': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['media_1'].widget.attrs.update({
            'class': 'form-control',
            'accept': 'image/*'
        })
        self.fields['media_2'].widget.attrs.update({
            'class': 'form-control',
            'accept': 'image/*'
        })
        self.fields['media_3'].widget.attrs.update({
            'class': 'form-control',
            'accept': 'image/*'
        })
