from django.urls import path
from . import views

urlpatterns = [
  path('', views.CardinfoList.as_view()),
  path('register/', views.CardinfoCreateView.as_view()),
  path('registerremote/', views.CardinfoCreateRemoteView.as_view()),
  path('<int:pk>/', views.CardinfoDetail.as_view()),
  path('<int:pk>/update', views.CardinfoUpdateView.as_view()),
  path('<int:pk>/delete/', views.CardinfoDeleteView.as_view()),
  # path('<int:pk>/clearcache/', views.ClientsClearcacheView.as_view()),
  # path('<int:pk>/remo_scs_cpf/', views.RemoStartChargeView.as_view()),
  # path('<int:pk>/remo_stop_cs/', views.RemoStopChargeView.as_view()),
  # path('<int:pk>/unlock_connector/', views.UnlockConnView.as_view()),
  # path('<int:pk>/getconf/', views.GetConfView.as_view()),
  # path('<int:pk>/setconf/', views.SetConfView.as_view()),
  # path('<int:pk>/reset/', views.ClientsResetView.as_view()),
  # path('<int:pk>/getcompositeschedule/', views.GetCmpScheduleView.as_view()),
  # path('<int:pk>/setchargingprofile/', views.SetChgProfileView.as_view()),
  # path('<int:pk>/clearchargingprofile/', views.ClearChgProfileView.as_view()),
  # path('simul/', views.index),
  # path('simul/<str:cpnumber>/', views.index),
]