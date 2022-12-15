from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("upload_file",file_handle,name="file_handle"),
    path("plot",plot,name="graph"),
]