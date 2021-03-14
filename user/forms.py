from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms.widgets import PasswordInput

from .models import Profile

User = get_user_model()

class  SignupForm(UserCreationForm):
    username = forms.CharField(label='اسم االمستخدم ', help_text='يجب ان  لا يحتوي على رموز خاصة او مسافات فارغة ')
    password1 = forms.CharField(min_length=8 ,widget=PasswordInput, help_text='يجب ان يحتوي على احرف كبيرة واحرف صغيرة وارقام ', label='كلمة مرور ')
    password2 = forms.CharField(min_length=8 ,widget=PasswordInput, help_text='تأكد من ان كلمة المرور متابقة  ', label='تأكيد كلمة المرور ')
    first_name = forms.CharField(max_length=150, required=False, label='الاسم الأول' ,help_text='اختياري')
    last_name = forms.CharField(max_length=150, required=False, label='الاسم الثاني' ,help_text='اختياري')
    email = forms.EmailField(max_length=254,label='البريد الالكتروني', help_text='تأكد من صحة البريد الالكتروني')


    class Meta:
        model = User
        fields = (
            'username', 'password1', 'password2', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('كلمة المرور غير متطابقة')
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('يوجد مستخدم مسجل بهذا الاسم.')
        return cd['username']
        

class UserFormUpdate(forms.ModelForm):
    first_name = forms.CharField(max_length=150, required=False, label='الاسم الأول' ,help_text='اختياري')
    last_name = forms.CharField(max_length=150, required=False, label='الاسم الثاني' ,help_text='اختياري')
    email = forms.EmailField(max_length=254,label='البريد الالكتروني', help_text='تأكد من صحة البريد الالكتروني')
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email'
        )


class profileFormUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'image',
        )
    

