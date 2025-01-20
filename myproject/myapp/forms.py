from django import forms
from .models import Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = [
            'number', 'weight', 'file1', 'date_delivery',
            'date_submission', 'submission_to_database',
            'shipment_date_time', 'withdrawal_from_bases', 'file2'
        ]
        widgets = {
            'date_delivery': forms.DateInput(attrs={'type': 'date'}),
            'date_submission': forms.DateInput(attrs={'type': 'date'}),
            'submission_to_database': forms.DateInput(attrs={'type': 'date'}),
            'shipment_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'withdrawal_from_bases': forms.DateInput(attrs={'type': 'date'}),
        }
