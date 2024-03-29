
#

from django import forms
from django.contrib.auth.models import User
from .models import Post

class TextForm(forms.ModelForm):
    stegtype = forms.CharField(max_length=10, widget=forms.HiddenInput(), initial='Text')
    CHOICES = (('1', 'Encrypt',), ('2', 'Decrypt'))
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, label='Choose Mode:', required=False, initial='1')
    plaintext = forms.CharField(label='Plain Text')
    hiddentext = forms.CharField(label='Hidden Text', max_length=35, required=False)


    class Meta:
        model = Post
        fields = ['stegtype', 'choice_field', 'plaintext', 'hiddentext']


class ImageForm(forms.ModelForm):
    stegtype = forms.CharField(max_length=10, widget=forms.HiddenInput(), initial='Text')
    stegimage = forms.ImageField(label="Image")
    hiddentext = forms.CharField(label='Hidden Text', max_length=35)

    class Meta:
        model = Post
        fields = ['stegtype', 'stegimage', 'hiddentext']

class AudioForm(forms.ModelForm):
    stegtype = forms.CharField(max_length=10, widget=forms.HiddenInput(), initial='Text')
    CHOICES = (('1', 'Encrypt',), ('2', 'Decrypt'))
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, label='Choose Mode:', required=False, initial='1')
    hiddentext = forms.CharField(label='Text')

    class Meta:
        model = Post
        fields = ['stegtype', 'choice_field', 'hiddentext']
