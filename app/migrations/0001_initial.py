# Generated by Django 2.0 on 2019-07-04 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_date', models.DateField()),
                ('match_ground', models.CharField(choices=[('Ahd', 'Ahmendabad'), ('Blr', 'Banglore'), ('Chn', 'Chennai'), ('Del', 'Delhi'), ('Jai', 'Jaipur'), ('Kol', 'Kolkata'), ('Moh', 'Mohali'), ('Mum', 'Mumbai')], max_length=3)),
                ('match_team2', models.CharField(max_length=50)),
                ('match_visit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50)),
                ('capt_name', models.CharField(max_length=50)),
                ('home_ground', models.CharField(choices=[('Ahd', 'Ahmendabad'), ('Blr', 'Banglore'), ('Chn', 'Chennai'), ('Del', 'Delhi'), ('Jai', 'Jaipur'), ('Kol', 'Kolkata'), ('Moh', 'Mohali'), ('Mum', 'Mumbai')], max_length=3)),
                ('coach_name', models.CharField(max_length=50)),
                ('poc', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='match_team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Team'),
        ),
    ]
