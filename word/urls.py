from django.contrib import admin
from word import views

from django.urls import path



urlpatterns=[
    path("numchanger",views.NumToWordView.as_view(),name='changer')
]