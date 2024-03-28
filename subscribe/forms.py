

from django import forms
from django.utils.translation import gettext_lazy as _

from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'
        labels={
            'first_name': _('Enter first name'),
            'last_name': _('Enter last name'),
            'email': _('Enter email')
        }
        # help_texts={'first_name':_('Enter only characters')}
        error_messages={
            'first_name':{
                'required':_('First name is mandatory'),
            },
        }
        


# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError("Invalid name")
#     return value

# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length= 100)
#     last_name = forms.CharField(max_length= 100, validators=[validate_comma])
#     email = forms.EmailField(max_length = 100, required=True, validators=[validate_comma])


    # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']
    #     if ',' in data:
    #         raise forms.ValidationError("Invalid First name")
    #     return data