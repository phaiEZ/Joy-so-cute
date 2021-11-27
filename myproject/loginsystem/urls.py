from django.urls import path
from .views import index, register
urlpatterns = [
    path('register', index, name="member"),
    path('register/add', register, name="addUser")
]
# name = name of this url
# /user/register
