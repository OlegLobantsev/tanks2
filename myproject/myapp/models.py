from django.db import models
from django.urls import reverse

class Record(models.Model):
    number = models.IntegerField(unique=True)
    weight = models.FloatField(blank=True, null=True)
    file1 = models.FileField(upload_to='files/', blank=True, null=True)
    date_delivery = models.DateTimeField()
    date_submission = models.DateTimeField()
    submission_to_database = models.DateTimeField()
    shipment_date_time = models.DateTimeField()
    withdrawal_from_bases = models.DateTimeField()
    file2 = models.FileField(upload_to='files/', blank=True, null=True)
    file3 = models.FileField(upload_to='files/', blank=True, null=True)
    file4 = models.FileField(upload_to='files/', blank=True, null=True)

    def get_days_late(self):
        if self.date_submission > self.date_delivery:
            delta = self.date_submission - self.date_delivery
            return delta.days
        return 0
    def get_days_total(self):
        delta = self.withdrawal_from_bases - self.date_submission
        return delta.days
    def get_delay_1(self):
        delta = self.submission_to_database - self.date_submission
        return delta.days
    def get_delay_2(self):
        delta = self.withdrawal_from_bases - self.shipment_date_time
        return delta.days

    def __str__(self):
        return f"Record {self.number}"

    def get_absolute_url(self):
        return reverse('record_list')