from django import forms

class CSVUploadForm(forms.Form):
    file = forms.FileField(label="Upload a CSV File", required=True)