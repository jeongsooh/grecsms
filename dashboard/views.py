from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
# from django.views.generic.edit import FormView

# from .models import Evcharger

from user.forms import LoginForm
# from .forms import EvchargerRegisterForm

# Create your views here.

def index(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      request.session['user'] = form.data.get('userid')
      return redirect('/dashboard')
  else:
    form = LoginForm()
  return render(request, 'index.html', {'form': form})

def logout(request):
  if 'user' in request.session:
    del(request.session['user'])

  return redirect('/')

def dashboard(request):
  user_id = request.session['user']
  return render(request, 'dashboard.html', {'loginuser': user_id})

