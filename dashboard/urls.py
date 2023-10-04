from django.urls import path
from . import views

urlpatterns = [
  path('', views.dashboard),
  # path('register/', views.EvchargerCreateView.as_view()),
  # path('<int:pk>/', views.EvchargerDetail.as_view()),
  # path('<int:pk>/update', views.EvchargerUpdateView.as_view()),
  # path('<int:pk>/delete/', views.EvchargerDeleteView.as_view()),
]