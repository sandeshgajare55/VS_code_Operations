from django.urls import path
from app_Ninad  import views

urlpatterns=[
path("Home/",views.home,name="Home")
#path("Away/",views.away,name="Away")
]