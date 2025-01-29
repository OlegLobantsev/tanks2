from django import forms
from .models import Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = [
            'number', 'weight', 'file1', 'date_delivery', 'delivery',
            'date_submission', 'submission_to_database',
            'shipment_date_time', 'withdrawal_from_bases', 'file3', 'file4', 'file2'
        ]
        widgets = {
            'date_delivery': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_submission': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'submission_to_database': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'shipment_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'withdrawal_from_bases': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }