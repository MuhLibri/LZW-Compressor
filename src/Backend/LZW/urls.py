from django.urls import path
from . import views

urlpatterns = [
    # path('', views.getData),
    # path('add/', views.addHistory),
    path('', views.index),
    path('history', views.getHistory)
]