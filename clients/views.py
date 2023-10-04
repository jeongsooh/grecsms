from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views.generic.edit import FormView

from django.db.models import Q

from .models import Clients
from .forms import ClientsResetForm, ChargingProfileForm, CompositeScheduleForm, ClearChargingProfileForm, RemoteStartForm

from ocpp16.client_gateway import ( reset_evcharger, update_evcharger, clearcache_evcharger, 
      remotestart_evcharger, remotestop_evcharger, unlock_connector, get_conf, set_conf,
      set_charging_profile, clear_charging_profile, get_composite_schedule)

# Create your views here.

class ClientsList(ListView):
  model = Clients
  template_name='clients.html'
  context_object_name = 'clientsList'
  paginate_by = 5
  queryset = Clients.objects.all()

  def get_queryset(self):
    queryset = Clients.objects.all()
    query = self.request.GET.get("q", None)
    if query is not None:
      queryset = queryset.filter(
        Q(cpnumber__icontains=query) |
        Q(cpstatus__icontains=query) |
        Q(channel_status_1__icontains=query)
      )
    return queryset

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    return context

class ClientsDeleteView(DeleteView):
    model = Clients
    template_name='clients_confirm_delete.html'
    success_url = '/clients'

class ClientsDetail(DetailView):
  template_name='clients_detail.html'
  queryset = Clients.objects.all()
  context_object_name = 'clients'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    
    return context

class ClientsClearcacheView(FormView):
  template_name = 'clients_reset.html'
  form_class = ClientsResetForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    clearcache_evcharger(cpnumber)

    return super().form_valid(form) 

class RemoStartChargeView(FormView):
  template_name = 'clients_reset.html'
  form_class = RemoteStartForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    id_tag = form.data.get('id_tag')
    charging_profile = form.data.get('charging_profile')

    remotestart_evcharger(cpnumber, id_tag, charging_profile)

    return super().form_valid(form) 

class RemoStopChargeView(FormView):
  template_name = 'clients_reset.html'
  form_class = ClientsResetForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    remotestop_evcharger(cpnumber)

    return super().form_valid(form) 

class UnlockConnView(FormView):
  template_name = 'clients_reset.html'
  form_class = ClientsResetForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    connector_id = form.data.get('connector_id')
    unlock_connector(cpnumber, connector_id)

    return super().form_valid(form) 

class GetConfView(FormView):
  template_name = 'clients_reset.html'
  form_class = ClientsResetForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    msg_content = form.data.get('msg_content')
    get_conf(cpnumber, msg_content)

    return super().form_valid(form) 

class SetConfView(FormView):
  template_name = 'clients_reset.html'
  form_class = ClientsResetForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    msg_content = form.data.get('msg_content')
    set_conf(cpnumber, msg_content)

    return super().form_valid(form) 

class ClientsResetView(FormView):
  template_name = 'clients_reset.html'
  form_class = ClientsResetForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    reset_type = form.data.get('reset_type')
    reset_evcharger(cpnumber, reset_type)

    return super().form_valid(form) 

# class ClientsFwupdateView(FormView):
#   template_name = 'clients_fwupdate.html'
#   form_class = ClientsResetForm
#   success_url = '/clients'

#   def form_valid(self, form):
#     cpnumber = form.data.get('cpnumber')
#     update_clients(cpnumber)

#     return super().form_valid(form) 


class GetCmpScheduleView(FormView):
  template_name = 'charging_profile.html'
  form_class = CompositeScheduleForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    connectorId = form.data.get('connector_id')
    duration = form.data.get('duration')

    get_composite_schedule(cpnumber, connectorId, duration)

    return super().form_valid(form) 

class SetChgProfileView(FormView):
  template_name = 'charging_profile.html'
  form_class = ChargingProfileForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    profile = {
      'connectorId': form.data.get('connector_id'),
      'chargingProfilePurpose': form.data.get('charging_profile_purpose'),      # ChargePointMaxProfile, TxDefaultProfile, TxProfile
      'chargingProfileKind': form.data.get('charging_profile_kind'),            # Absolute, Recurring, Relative 
      'chargingProfileId': 1,
      'stackLevel': 1,
      'chargingSchedule': {
        'duration': int(form.data.get('duration')),
        'chargingRateUnit': 'W',
        'chargingSchedulePeriod': [
          {
            'startPeriod': 1,
            'limit': 8.1,
          },
        ]
      }
    }
    set_charging_profile(cpnumber, profile)

    return super().form_valid(form) 

class ClearChgProfileView(FormView):
  template_name = 'charging_profile.html'
  form_class = ClearChargingProfileForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    connectorId = form.data.get('connector_id')
    id = form.data.get('profile_id')

    clear_charging_profile(cpnumber, connectorId, id)

    return super().form_valid(form) 