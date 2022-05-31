from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('grade/', views.note_calculator),
    path('grade/reset/', views.note_calculator_reset),
    path('username/', views.username),
    path('dice/', views.dice),
    path('tipping/end/', views.tipping_pace_end),
    path('tipping/', views.tipping_pace_start),
    path('password/', views.password),
]


