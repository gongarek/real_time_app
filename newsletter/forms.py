from django import forms
from .models import SignUp



class ContactForm(forms.Form):
    nazwa = forms.CharField(required=False)
    email = forms.EmailField()
    informacja = forms.CharField(widget=forms.Textarea)



class SignUpForm(forms.ModelForm):
    prezentacja = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = SignUp
        fields = ['full_name', 'email', 'prezentacja' ]

    def clean_email(self):
        email =  self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        if not "pw.edu.pl" in provider :
            raise forms.ValidationError("Napisz e-mail PW ")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if not " " in full_name :
            raise forms.ValidationError("Podaj imie i nazwisko")
        return full_name

    # def clean_wiadomosc(self):
    #     wiadomosc = self.cleaned_data.get('wiadomosc')
    #     return wiadomosc
