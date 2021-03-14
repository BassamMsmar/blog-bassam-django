from django import forms
from .models import Comment, Post



class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(max_length=100,label='العنوان' )
    content = forms.CharField(label='محتوى المقال')

    class Meta:
        model = Post
        fields = ('title', 'content')







