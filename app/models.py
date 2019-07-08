from django.db import models

# Create your models here.
# grounds= ('Ahmedabad','Bangalore','Chennai','Delhi','Jaipur','Kolkata','Mohali','Mumbai')
grounds = (
    ('Ahd','Ahmendabad'),
    ('Blr','Banglore'),
    ('Chn','Chennai'),
    ('Del','Delhi'),
    ('Jai','Jaipur'),
    ('Kol','Kolkata'),
    ('Moh','Mohali'),
    ('Mum','Mumbai'),
)

class Team(models.Model):
    team_name = models.CharField(max_length=50)
    capt_name = models.CharField(max_length=50)
    home_ground = models.CharField(max_length=15,choices=grounds)
    coach_name = models.CharField(max_length=50)
    poc = models.IntegerField()

class Match(models.Model):
    match_date = models.DateField()
    match_ground = models.CharField(max_length=15,choices=grounds)
    match_team1 = models.CharField(max_length=50)
    match_team2 = models.CharField(max_length=50)
    match_visit = models.IntegerField()


