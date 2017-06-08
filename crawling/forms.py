'''
Created on May 16, 2017

@author: Asus-PC
'''
from django import forms

class PostForm(forms.Form):
    url1 = forms.CharField(max_length=256)
    keyword1 = forms.CharField(max_length=256)

class UploadForm(forms.Form):
    file1 = forms.FileField()
 