from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *
# Create your views here.
def MainPage(request):
    return render(request,"app/main.html")
def MatchPage(request):
    return render(request,"app/reg_team.html")
def TeamPage(request):
    return render(request,"app/reg_match.html")

def RegisterTeam(request):
    team_name=request.POST['team_name']
    capt_name=request.POST['capt_name']
    home_ground=request.POST['grounds']
    coach_name=request.POST['coach_name']
    poc=request.POST['poc']

    newuser= Team.objects.create(team_name=team_name,capt_name=capt_name,home_ground=home_ground,coach_name=coach_name,poc=poc)
    return render(request,"app/successteam.html")

def RegisterMatch(request):
    match_date=request.POST['match_date']
    match_ground=request.POST['grounds']
    match_team1=request.POST['match_team1']
    match_team2=request.POST['match_team2']
    match_visit=request.POST['match_visit']

    newuser= Match.objects.create(match_date=match_date,match_ground=match_ground,match_team1=match_team1,match_team2=match_team2,match_visit=match_visit)
    return HttpResponseRedirect(reverse('showmatch'))


def ShowMatch(request):

    all_match = Match.objects.all()
    print("All Match ---------->",all_match)
    return render(request,"app/show.html",{'all_match':all_match})