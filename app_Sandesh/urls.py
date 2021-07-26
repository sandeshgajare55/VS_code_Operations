from django.urls import path
from .import  views

urlpatterns=[
path("Home/",views.yamaha,name="Ym"),
path("Away/",views.tvs,name='tvs')
  #  path('', views.yamaha,name=("Yamaha"))
]