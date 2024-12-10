from django import forms

class CSVUploadForm(forms.Form):
    file = forms.FileField(
        widget=forms.FileInput(attrs={
            'id': 'file-upload',
            'class': 'sr-only',
            'accept': '.csv'
        })
    )
