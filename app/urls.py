from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.MainPage,name="main"),
    path("reg_team/",views.MatchPage,name="reg_team"),
    path("reg_match/",views.TeamPage,name="reg_match"),

    path("registerteam/",views.RegisterTeam,name="registerteam"),
    path("registermatch/",views.RegisterMatch,name="registermatch"),
    path("showmatch/",views.ShowMatch,name="showmatch"),
]
