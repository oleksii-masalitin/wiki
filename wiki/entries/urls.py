from django.urls import path

from . import views

urlpatterns = [
    path("<str:entry>", views.index, name="index")
]