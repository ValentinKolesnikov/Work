from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:id>', views.event, ),
    path('create/', views.create),
    path('like', views.like,),
]
