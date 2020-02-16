from django import forms
from .models import Document, Short, Youtube, Stegano,FaceRecognition


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        fields = ('folder', 'file', 'password',)


class ShortForm(forms.ModelForm):
    class Meta:
        model = Short
        fields = ('url', 'name')


class YoutubeForm(forms.ModelForm):
    class Meta:
        model = Youtube
        fields = ('url',)

class SteganoForm(forms.ModelForm):
    class Meta:
        model = Stegano
        fields = ('message','picture', 'key', )

class FaceForm(forms.ModelForm):
    class Meta:
        model = FaceRecognition
        fields = ('picture',)
 