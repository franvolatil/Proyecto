from django import forms
from .models import Post
from .models import Sismo

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class SismoForm(forms.ModelForm):
    class Meta:
        model = Sismo
        fields = ('title',)