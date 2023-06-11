from django import forms
from .models import Editor
from ckeditor.widgets import CKEditorWidget
class EditorForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(),label="Text Editor")
    a=5
    b=a
    class Meta:
        model=Editor
        fields="__all__"