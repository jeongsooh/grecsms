from django.urls import path
from . import views

urlpatterns = [
  path('', views.apiOverview, name='api-overview'),
  path('msgapilist/', views.MsgapiList.as_view(), name='Msgapi-List'),
  path('msgapi-list/', views.msgapiList, name='msgapi-list'),
  path('msgapi-detail/<str:pk>/', views.msgapiDetail, name='msgapi-detail'),
  path('msgapi-create/', views.msgapiCreate, name='msgapi-create'),
  path('msgapi-update/<str:pk>/', views.msgapiUpdate, name='msgapi-update'),
  path('msgapi-delete/<str:pk>/', views.msgapiDelete, name='msgapi-delete'),
]