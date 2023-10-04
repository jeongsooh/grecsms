from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
# from django.views.generic.edit import FormView

# from django.db.models import Q

from .models import Evcharger

from user.forms import LoginForm
from .forms import EvchargerRegisterForm
# EvchargerResetForm, EvchargerFilterForm
# from .filters import EvchargerFilter

# from ocpp16.client_gateway import reset_evcharger, update_evcharger

# Create your views here.

def index(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      request.session['user'] = form.data.get('userid')
      return redirect('/evcharger')
  else:
    form = LoginForm()
  return render(request, 'index.html', {'form': form})

def logout(request):
  if 'user' in request.session:
    del(request.session['user'])

  return redirect('/')

class EvchargerList(ListView):
  model = Evcharger
  template_name='evcharger.html'
  context_object_name = 'evchargerList'
  paginate_by = 2
  queryset = Evcharger.objects.all()

  def get_queryset(self):
    queryset = Evcharger.objects.all()
    query = self.request.GET.get("q", None)
    if query is not None:
      queryset = queryset.filter(
        Q(cpstatus__icontains=query) |
        Q(cpnumber__icontains=query) |
        Q(cpsite__icontains=query) |
        Q(register_dttm__icontains=query)
      )
    return queryset

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id

    return context

class EvchargerDetail(DetailView):
  template_name='evcharger_detail.html'
  queryset = Evcharger.objects.all()
  context_object_name = 'evcharger'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    
    return context

class EvchargerUpdateView(UpdateView):
  model = Evcharger
  template_name='evcharger_update.html'
  fields = ['cpnumber', 'cpsite', 'address', 'partner_id', 'manager_id', 'public_use', 'fwversion','cpstatus', 'cpmodel', 'cpmaker']
  success_url = '/evcharger'

class EvchargerCreateView(CreateView):
  model = Evcharger
  # form_class = EvchargerRegisterForm
  template_name = 'evcharger_register.html'
  fields = ['cpnumber', 'cpsite', 'address', 'partner_id', 'manager_id', 'public_use', 'fwversion','cpstatus', 'cpmodel', 'cpmaker']
  success_url = '/evcharger'

class EvchargerDeleteView(DeleteView):
    model = Evcharger
    template_name='evcharger_confirm_delete.html'
    success_url = '/evcharger'

# class EvchargerResetView(FormView):
#   template_name = 'evcharger_reset.html'
#   form_class = EvchargerResetForm
#   success_url = '/evcharger'

#   def form_valid(self, form):
#     cpnumber = form.data.get('cpnumber')
#     reset_evcharger(cpnumber)

#     return super().form_valid(form) 

# class EvchargerFwupdateView(FormView):
#   template_name = 'evcharger_fwupdate.html'
#   form_class = EvchargerResetForm
#   success_url = '/evcharger'

#   def form_valid(self, form):
#     cpnumber = form.data.get('cpnumber')
#     update_evcharger(cpnumber)

#     return super().form_valid(form) 

