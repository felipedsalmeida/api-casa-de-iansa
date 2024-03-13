from django.urls import path
from .views import MediumView

urlpatterns = [path("mediuns/", MediumView.as_view())]
