from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username= forms.CharField(max_length=100,label='mail adresiniz')
    password= forms.CharField(max_length=100,label='Parola',widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Kullanıcı adını veya şifreyi yanlış girdiniz!")
        return super(LoginForm, self).clean()

class RegisterForm(forms.Form):

    user = forms.CharField(max_length=100, label='Kullanıcı Adı')
    password1 = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='Parola Doğrulama', widget=forms.PasswordInput)
    onay = forms.BooleanField()

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]
###############################
    # username = forms.CharField(max_length=50, label="Kullanıcı Adı")
    # password = forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)
    # confirm = forms.CharField(max_length=20, label="Parolayı Doğrula", widget=forms.PasswordInput)
    #
    # def clean(self):
    #     username = self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")
    #     confirm = self.cleaned_data.get("confirm")
    #
    #     if password and confirm and password != confirm:
    #         raise forms.ValidationError("Parolalar Eşleşmiyor")
    #
    #     values = {
    #         "username": username,
    #         "password": password
    #     }
    #     return values
################################
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        onay = self.cleaned_data.get("onay")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Şifreler eşleşmiyor!")
        if not onay:
            raise forms.ValidationError("Lütfen onay işlemini yapınız")
        return password2
