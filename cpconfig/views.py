from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.db.models import Q

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView

from .models import Cpconfig
from .serializers import CpconfigSerializer

@csrf_exempt
def cpconfig_list(request):
    """
    List all code cpconfigs, or create a new cpconfig.
    """
    if request.method == 'GET':
      data = request.GET.get('ID')
      cpconfigs = Cpconfig.objects.filter(cpserial=data)
      if cpconfigs:
        cpnumber = cpconfigs.values()[0]['cpnumber']
        conf_info = {
          "url":"ws://3.37.224.145:80/ws/ocpp/",
          "cpId":cpnumber,
        }
        return JsonResponse(conf_info)
      cpconfigs = Cpconfig.objects.all()
      serializer = CpconfigSerializer(cpconfigs, many=True)
      return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
      data = JSONParser().parse(request)
      serializer = CpconfigSerializer(data=data)
      if serializer.is_valid():
          serializer.save()
          return JsonResponse(serializer.data, status=201)
      return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def cpconfig_detail(request, pk):
    """
    Retrieve, update or delete a code cpconfig.
    """
    try:
        cpconfig = Cpconfig.objects.get(pk=pk)
    except Cpconfig.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CpconfigSerializer(cpconfig)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CpconfigSerializer(cpconfig, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cpconfig.delete()
        return HttpResponse(status=204)

class CpconfigViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cpconfigs to be viewed or edited.
    """
    queryset = Cpconfig.objects.all()
    serializer_class = CpconfigSerializer
    permission_classes = [permissions.IsAuthenticated]

class CpconfigList(ListView):
  model = Cpconfig
  template_name='cpconfig.html'
  context_object_name = 'cpconfigList'
  paginate_by = 10
  queryset = Cpconfig.objects.all()

  def get_queryset(self):
    queryset = Cpconfig.objects.all()
    query = self.request.GET.get("q", None)
    if query is not None:
      queryset = queryset.filter(
        Q(cpnumber__icontains=query) |
        Q(cpserial__icontains=query)
      )
    return queryset

class CpconfigRegisterView(CreateView):
  model = Cpconfig
  template_name = 'cpconfig_register.html'
  fields = ['cpnumber', 'cpserial']
  success_url = '/cpconfig'

class CpconfigDeleteView(DeleteView):
    model = Cpconfig
    template_name='cpconfig_confirm_delete.html'
    success_url = '/cpconfig'

class CpconfigUpdateView(UpdateView):
  model = Cpconfig
  template_name='cpconfig_update.html'
  fields = ['cpnumber', 'cpserial']
  success_url = '/cpconfig'