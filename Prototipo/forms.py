from django import forms
from Prototipo.models import Post, UploadFile
from Prototipo.models import Sismo

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class SismoForm(forms.ModelForm):
    class Meta:
        model = Sismo
        fields = ('title',)

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ('title','media',)