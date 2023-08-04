from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "LandingPage.html")

def schedule(request):
    return render(request, "Schedule.html")

def teams(request):
    return render(request, "Teams.html")

def stats(request):
    return render(request, "Stats.html")

def register(request):
    return render(request, "Register.html")

def about(request):
    return render(request, "About.html")

def boxScore(request):
    return render(request, "Boxscore.html")

def allStats(request):
    return render(request, "AllStats.html")

def login(request):
    return render(request, "Login.html")

def adminSchedule(request):
    return render(request, "Admin_Schedule.html")

def adminRegister(request):
    return render(request, "Admin_Register.html")

def adminTeams(request):
    return render(request, "Admin_Teams.html")

def adminTeams2(request):
    return render(request, "Admin_Register2.html")

def adminAccounts(request):
    return render(request, "Admin_Accounts.html")

def adminRegister2(request):
    return render(request, "Admin_Register2.html")

def adminAccounts2(request):
    return render(request, "Admin_Accounts2.html")

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import PlayerForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = PlayerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PlayerForm()

    return render(request, "register.html", {"form": form})