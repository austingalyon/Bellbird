from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ChirpForm
from .models import Chirp
import requests

# Create your views here.
def home_view(request):
  queryset = Chirp.objects.all()
  context = {
    "chirps": queryset
  }
  return render(request, "home.html", context)

def chirp_create_view(request):
  form = ChirpForm(request.POST or None)
  if form.is_valid():
    new_chirp = form.save()
    form = ChirpForm()
    r = requests.post('https://bellbird.joinhandshake-internal.com/push', data = {'chirp_id':new_chirp.id})
    return HttpResponseRedirect('/index/')
  context = {
    'form': form
  }
  return render(request, "chirp_create.html", context)