from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import authenticate
from django.db import models

from account.models import Account,Territory


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Pochta manzili',max_length=254, help_text='To`ldirish shart')
    username=forms.CharField(label='Username')
    phone_number=forms.CharField(label='Telefon raqam',max_length=100)
    territory=forms.ModelChoiceField(label='Xudud',empty_label='Xudud tanlang',queryset=Territory.objects.all())
    password=forms.CharField(label="Parol",widget=forms.PasswordInput())
    class Meta:
        model = Account
        fields = ('email', 'username', 'password','phone_number','territory')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('email','phone_number')

class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Kirishda xatolik aniqlandi!")


class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = Account
		fields = ('email', 'username','phone_number',)

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email
		raise forms.ValidationError('Bu Email "%s" band!.' % account)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
		except Account.DoesNotExist:
			return username
		raise forms.ValidationError('Bu Username "%s" band!.' % username)
















