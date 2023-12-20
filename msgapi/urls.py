from django.urls import path
from . import views

urlpatterns = [
  path('', views.apiOverview, name='api-overview'),
  path('msgapilist/', views.MsgapiList.as_view(), name='Msgapi-List'),
  path('msgapi-list/', views.msgapiList, name='msgapi-list'),
  path('pvapi-list/', views.pvapiList, name='pvapi-list'),
  path('msgapi-detail/<str:pk>/', views.msgapiDetail, name='msgapi-detail'),
  path('pvapi-detail/<str:pk>/', views.pvapiDetail, name='pvapi-detail'),
  path('msgapi-create/', views.msgapiCreate, name='msgapi-create'),
  path('pvapi-create/', views.pvapiCreate, name='pvapi-create'),
  path('pvapi-create2', views.pv2apiCreate, name='pvapi-create'),
  path('msgapi-update/<str:pk>/', views.msgapiUpdate, name='msgapi-update'),
  path('msgapi-delete/<str:pk>/', views.msgapiDelete, name='msgapi-delete'),
  path('pvapi-delete/<str:pk>/', views.pvapiDelete, name='pvapi-delete'),
]