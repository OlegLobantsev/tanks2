# Generated by Django 5.1.5 on 2025-01-17 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('weight', models.FloatField()),
                ('file1', models.FileField(blank=True, null=True, upload_to='files/')),
                ('date_delivery', models.DateField()),
                ('date_submission', models.DateField()),
                ('submission_to_database', models.DateField()),
                ('shipment_date_time', models.DateTimeField()),
                ('withdrawal_from_bases', models.DateField()),
                ('file2', models.FileField(blank=True, null=True, upload_to='files/')),
            ],
        ),
    ]
