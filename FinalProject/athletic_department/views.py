from django.shortcuts import render, redirect
from .models import Team
from django.views import View
from .models import Team
from .forms import TeamForm


def homepage(request):
    return render(request, 'athletic_department/Homepage.html')

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'athletic_department/team_list.html', {'teams': teams})

class TeamList(View):
    def get(self, request):
        teams = Team.objects.all()
        return render(request, 'athletic_department/team_list.html', {'teams': teams})


class TeamEdit(View):
    def get(self, request, team_id=None):
        if team_id:
            team = Team.objects.get(pk=team_id)
        else:
            team = Team()
        form = TeamForm(instance=team)
        return render(request, 'athletic_department/team_edit.html', {'team': team, 'form': form})

    def post(self, request, team_id=None):
        if team_id:
            team = Team.objects.get(pk=team_id)
        else:
            team = Team()
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team-list')
        return render(request, 'athletic_department/team_edit.html', {'team': team, 'form': form})

class TeamDelete(View):
    def get(self, request, team_id=None):
        team = Team.objects.get(pk=team_id)
        form = TeamForm(instance=team)
        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True
        return render(request, 'athletic_department/team_delete.html', {'team': team, 'form': form})

    def post(self, request, team_id=None):
        team = Team.objects.get(pk=team_id)
        team.delete()
        return redirect('team-list')