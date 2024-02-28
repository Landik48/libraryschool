from .models import wishes
from django.forms import ModelForm, Textarea

class wishesForm(ModelForm):
    class Meta:
        model = wishes
        fields = ['title', 'description']
        widgets = {
            'title': Textarea(attrs={
                'class': 'title',
                'placeholder': 'Краткое описание',
                'style': 'resize: none;'
            }),
            'description': Textarea(attrs={
                'class': 'description',
                'placeholder': 'Подробное описание'
            })
        }