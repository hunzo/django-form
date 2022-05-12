from django import forms
from ckeditor.widgets import CKEditorWidget

class add_post_form(forms.Form):
    title = forms.CharField(label="CharField")
    content = forms.CharField(widget=CKEditorWidget(), label="RichTextField")
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))