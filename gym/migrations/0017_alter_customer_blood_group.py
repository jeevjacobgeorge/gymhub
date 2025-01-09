# Generated by Django 5.0.6 on 2024-12-06 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0016_customer_health'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('A1+', 'A1+'), ('A1-', 'A1-'), ('A2+', 'A2+'), ('A2-', 'A2-'), ('A1B+', 'A1B+'), ('A1B-', 'A1B-'), ('A2B+', 'A2B+'), ('A2B-', 'A2B-'), ('BOMBAY', 'BOMBAY')], max_length=6),
        ),
    ]