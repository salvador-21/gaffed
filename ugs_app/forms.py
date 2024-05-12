from django import forms
import django.forms.utils
import django.forms.widgets
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import UserAccount,UserWallet,Games
from django.contrib.auth.password_validation import validate_password
from django.core import validators

class LoginForm(forms.Form):
    username=forms.CharField(label="Username",max_length=50, widget=forms.TextInput(attrs={'autocomplete':'off','placeholder':'Username','class':'form-control mb-4 input-lg'}))
    password=forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control mb-4 input-lg '}))

class SignUpForm(forms.ModelForm):
    username=forms.CharField(label='Username',max_length=50, widget=forms.TextInput(attrs={'placeholder':'Username','class':'form-control '}))
    password = forms.CharField(max_length=50, widget = forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control pass1'}))
    confirm_password = forms.CharField(max_length=50, widget = forms.PasswordInput(attrs={'placeholder':' Confirmation','class':'form-control pass2'}))
    class Meta:
        model = User
        fields = ('username', 'password')

GENDER=(
    ('','SELECT GENDER'),
    ('MALE','MALE'),
    ('FEMALE','FEMALE')
)
USERTYPE=(
    ('','-------'),
    ('PLAYER','PLAYER'),
    ('AGENT','AGENT'),
    ('LOADER','LOADER'),
    ('DECLARATOR','DECLARATOR'),
    ('ADMIN','ADMIN'),
)

WALLET_STATUS=(
    ('ACTIVE','ACTIVE'),
    ('ONHOLD','ONHOLD'),
    ('BANNED','BANNED'),
)
GAMES=(
    ('E-SABONG','E-SABONG'),
    ('BALL GAMES','BALL GAMES'),
)

class UserForm(ModelForm):
    contact_no=forms.IntegerField(label='Contact', widget=forms.NumberInput(attrs={'minlength':'10','placeholder':'Mobile Number','class':'form-control'}))
    usertype=forms.ChoiceField(label='Account Type',widget=forms.Select(attrs={'class':'form-control bg-dark'}), choices=USERTYPE)
    class Meta:
        model = UserAccount
        fields=('contact_no',)

class WalletForm(ModelForm):
    w_balance=forms.IntegerField(label='Balance', widget=forms.NumberInput(attrs={'maxlength':'2','placeholder':'0','class':'form-control'}))
    w_points=forms.IntegerField(label='Points', widget=forms.NumberInput(attrs={'maxlength':'2','placeholder':'0','class':'form-control'}))
    w_commission=forms.IntegerField(label='Commission', widget=forms.NumberInput(attrs={'maxlength':'2','placeholder':'0','class':'form-control'}))
    w_status=forms.ChoiceField(label='Status',widget=forms.Select(attrs={'class':'form-control '}), choices=WALLET_STATUS)
    class Meta:
        model = UserWallet
        fields=('w_balance','w_points','w_commission',)


class GameForm(ModelForm):
    g_name=forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder':'Title','class':'form-control'}))
    g_desc=forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows':'5','class':'form-control'}))
    g_category=forms.ChoiceField(label='Status',widget=forms.Select(attrs={'class':'form-control '}), choices=GAMES)
    g_link=forms.CharField(label='Game Url', widget=forms.TextInput(attrs={'placeholder':'Url','class':'form-control'}))
    g_image=forms.FileField(label='Event Image', widget=forms.FileInput(attrs={'class':'form-control'}))
    class Meta:
        model = Games
        fields=('g_name','g_desc','g_category','g_link','g_image')