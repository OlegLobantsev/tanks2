from django import forms
from .models import Record

# Константа для хранения списка полей
FIELDS = [
    'number', 'weight', 'file1', 'date_delivery',
    'date_submission', 'submission_to_database',
    'shipment_date_time', 'withdrawal_from_bases', 'file2', 'file3', 'file4'
]

# Константа для хранения словаря виджетов
DATETIME_WIDGETS = {
    'date_delivery': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    'date_submission': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    'submission_to_database': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    'shipment_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    'withdrawal_from_bases': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
}

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = FIELDS  # Используем константу для списка полей
        widgets = DATETIME_WIDGETS  # Используем константу для виджетов

        # Если нужно добавить дополнительные настройки виджетов или другие метаданные,
        # их можно указать здесь
        # Например:
        # labels = {
        #     'number': 'Номер записи',
        # }