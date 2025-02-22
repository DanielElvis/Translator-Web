from django import forms
from django.core import validators
from . import langs


class TranslatorForm(forms.Form):
    lang = langs.langs_list
    user_text = forms.CharField(
        required=True , 
        widget = forms.TextInput(attrs = {
            "class" : "user-text-input",
            "placeholder" : "Your text :"
        }),

        validators=[
            validators.MinLengthValidator(0 , "Lenght Error : Please Enter Text"),
            validators.MaxLengthValidator(3000 , "Lenght Error")
        ],
        
        error_messages={
            "required" : "Please Enter A Word"
        })



    select_lang = forms.ChoiceField(
        choices=lang,
        label="Language",
        widget=forms.Select(
            attrs={
                "class" : "select-lang-input"
            }
        )
    )

