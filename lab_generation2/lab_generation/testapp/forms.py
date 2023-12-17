from django import forms
from django.contrib.auth.models import User
from django.forms import formset_factory


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли отличаются')
        return cd['password2']
    

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class MainPage(forms.Form):
    group = forms.CharField(label="Введите номер группы")
    fio = forms.CharField(label="Введите ФИО")
    fio2 = forms.CharField(label="Введите телефон")
    mission = forms.CharField(label="Назовите причину выдачи стипендии")
    num_ch = forms.CharField(label="Перечень документов")
    mun_ch = forms.CharField(label="Перечень документов")
    luma_ch = forms.CharField(label="Перечень документов")
    sun_ch = forms.CharField(label="Дата назначения стипендии")
    lun_ch = forms.CharField(label="Дата окончания стипендии")
    stipend_ch = forms.CharField(label="Дата назначения прошлой стипендии")
    step_ch = forms.CharField(label="Дата окончания прошлой стипендии")
    pric_ch = forms.CharField(label="Номер приказа")
    dat_ch = forms.CharField(label="Дата от начала приказа")



class CharapterBaseForm(forms.Form):
    charapter = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    #images = forms.CharField()
    #ChapterInfoSet