from django.db import models
from django.urls import reverse

class Record(models.Model):
    number = models.IntegerField(unique=True)
    weight = models.FloatField()
    file1 = models.FileField(upload_to='files/', blank=True, null=True)
    date_delivery = models.DateField()
    date_submission = models.DateField()
    submission_to_database = models.DateField()
    shipment_date_time = models.DateTimeField()
    withdrawal_from_bases = models.DateField()
    file2 = models.FileField(upload_to='files/', blank=True, null=True)

    def get_days_late(self):
        if self.date_submission > self.date_delivery:
            delta = self.date_submission - self.date_delivery
            return delta.days
        return 0

    def __str__(self):
        return f"Record {self.number}"

    def get_absolute_url(self):
        return reverse('record_list')