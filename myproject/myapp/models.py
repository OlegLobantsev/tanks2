from django.db import models
from django.urls import reverse
from datetime import timedelta

class Record(models.Model):
    number = models.IntegerField()
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
    # delivery = models.IntegerField(default=5)

    def get_difference(self) -> int:
        difference = (self.date_submission - self.date_delivery).days
        return difference if difference >= 0 else 0

    # def get_days_late(self) -> int:
    #     difference = self.get_difference()
    #     return max(difference - self.delivery, 0)

    def get_days_total(self) -> int:
        return self.get_delay_1() + self.get_delay_2()

    def get_delay_1(self) -> int:
        if self.submission_to_database and self.date_submission:
            delta = self.submission_to_database - self.date_submission
            return max(delta.days, 0) if delta.total_seconds() >= 0 else 0
        return 0

    def get_delay_2(self) -> int:
        if self.withdrawal_from_bases and self.shipment_date_time:
            delta = self.withdrawal_from_bases - self.shipment_date_time
            if delta.total_seconds() <= 23 * 3600:
                return 0
            late_seconds = delta.total_seconds() - 23 * 3600
            return int(late_seconds // 86400) + (1 if late_seconds % 86400 else 0)
        return 0

    def __str__(self) -> str:
        return f"Record {self.number}"

    def get_absolute_url(self) -> str:
        return reverse('record_list')