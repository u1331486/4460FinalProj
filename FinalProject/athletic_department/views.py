from django.shortcuts import render, redirect
from .models import Team
from django.views import View
from .forms import TeamForm


def homepage(request):
    return render(request, 'athletic_department/Homepage.html')

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'athletic_department/team_list.html', {'teams': teams})

class TeamCreateView(View):
    def get(self, request):
        form = TeamForm()
        return render(request, 'athletic_department/team_form.html', {'form': form})
    
    def post(self, request):
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_list')  
        return render(request, 'athletic_department/team_form.html', {'form': form})

class TeamUpdateView(View):
    def get(self, request, pk):
        team = Team.objects.get(pk=pk)
        form = TeamForm(instance=team)
        return render(request, 'athletic_department/team_form.html', {'form': form})

    def post(self, request, pk):
        team = Team.objects.get(pk=pk)
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_list')
        return render(request, 'athletic_department/team_form.html', {'form': form})

class TeamDeleteView(View):
    def get(self, request, pk):
        team = Team.objects.get(pk=pk)
        return render(request, 'athletic_department/team_confirm_delete.html', {'team': team})

    def post(self, request, pk):
        team = Team.objects.get(pk=pk)
        team.delete()
        return redirect('team_list')