# Generated by Django 2.0 on 2019-07-05 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190704_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_ground',
            field=models.CharField(choices=[('Ahd', 'Ahmendabad'), ('Blr', 'Banglore'), ('Chn', 'Chennai'), ('Del', 'Delhi'), ('Jai', 'Jaipur'), ('Kol', 'Kolkata'), ('Moh', 'Mohali'), ('Mum', 'Mumbai')], max_length=15),
        ),
        migrations.AlterField(
            model_name='team',
            name='home_ground',
            field=models.CharField(choices=[('Ahd', 'Ahmendabad'), ('Blr', 'Banglore'), ('Chn', 'Chennai'), ('Del', 'Delhi'), ('Jai', 'Jaipur'), ('Kol', 'Kolkata'), ('Moh', 'Mohali'), ('Mum', 'Mumbai')], max_length=15),
        ),
    ]
