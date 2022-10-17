from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from blog.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title_tag', 'title', 'body', 'author', 'category', 'post_image']

        widgets = {
            'title_tag':forms.TextInput(attrs={'class':'form-content', 'placeholder':'Title Tag'}),
            'title': forms.Textarea(attrs={'class': 'form-content', 'placeholder': 'Title'}),
            'body': forms.Textarea(attrs={'class': 'form-content'}),
            'author': forms.Select(attrs={'class': 'form-content'}),
            'category': forms.Select(attrs={'class': 'form-content'}),
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title_tag', 'title', 'body', 'category', 'post_image']

        widgets = {
            'title_tag':forms.TextInput(attrs={'class':'form-content', 'placeholder':'Title Tag'}),
            'title': forms.Textarea(attrs={'class': 'form-content', 'placeholder': 'Title'}),
            'body': forms.Textarea(attrs={'class': 'form-content'}),
            'category': forms.Select(attrs={'class': 'form-content'}),
        }


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
