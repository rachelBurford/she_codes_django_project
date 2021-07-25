from django import forms
from django.forms import ModelForm, fields, widgets
from .models import NewsStory


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title','author','pub_date','content']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
        }

# class StoryForm(ModelForm):
#     class Meta:
#         def __init__(self,*args, **kwargs):
#             super(StoryForm, self).__init__(*args, **kwargs)
#             self.fields['myfield'].widget.attrs.update({'class': 'myfieldclass'})

class MyForm(forms.Form):
    myfield = forms.CharField(widget=forms.TextInput(attrs={'class':'myfieldclass'}))
