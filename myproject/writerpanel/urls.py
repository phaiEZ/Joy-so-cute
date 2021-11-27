from django.urls import path
from .views import displayForm, panel
urlpatterns = [
    path('', panel, name="panel"),
    path('displayForm', displayForm, name="displayForm")
]
