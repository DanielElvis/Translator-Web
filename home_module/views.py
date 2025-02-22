from django.shortcuts import render
from django.views.generic import View
from .forms import TranslatorForm
from deep_translator import GoogleTranslator

# Create your views here.




class Translator(View):

    def translate_func(lang : str , text : str):
        translate = GoogleTranslator(target=lang).translate(text)
        return translate

    def get(self , request):
        translate_form = TranslatorForm()

        return render(request , "home_module/main.html" , {
            "translate_form" : translate_form
        })
    

    def post(self , request):

        translate_form = TranslatorForm(request.POST)

        if translate_form.is_valid():
            user_text = translate_form.cleaned_data.get("user_text")
            user_lang = translate_form.cleaned_data.get("select_lang")

            translate_user_text = Translator.translate_func(user_lang , user_text)

        return render(request , "home_module/main.html" , {
            "translate_form" : translate_form,
            "text" : translate_user_text
        })
