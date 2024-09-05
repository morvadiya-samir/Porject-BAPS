from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from core.forms import HaribhaktForm
from .models import Haribhakt
from mandal.models import Mandal

def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = HaribhaktForm(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('haribhakt.index')

        else:
            data = Haribhakt.objects.all().values()
            mandals = Mandal.objects.all().values()
            return render(request, 'haribhakt/index.html', {'data': data, 'mandals': mandals})
    else:
        return redirect("login")

@login_required
def create(request):
        form = HaribhaktForm()
        return render(request, 'haribhakt/create.html', {'form': form})


@login_required
def update(request,id):
    if request.method == 'POST':
        haribhakt = Haribhakt.objects.get(id = id)
        form = HaribhaktForm(request.POST,instance = haribhakt)
        if(form.is_valid()):
            form.save()
            return redirect('haribhakt.index')

@login_required
def edit(request, id):
        if request.method == 'GET':
            haribhakt = Haribhakt.objects.get(id=id)
            form = HaribhaktForm(instance=haribhakt)
            return render(request, 'haribhakt/edit.html', {'data': form,'id':id})
