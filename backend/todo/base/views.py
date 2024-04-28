from django.shortcuts import render
from rest_framework import viewsets

from base.models import Todolist
from base.models import Users


from base.serialiazers import User_serilaizers
from base.serialiazers import Todolist_serilaizers



# Create your views here.



class user_viewsets(viewsets.ModelViewSet):
    queryset =Users.objects.all()
    serializer_class=User_serilaizers

class todolist_viewsets(viewsets.ModelViewSet):
    queryset =Todolist.objects.all()
    serializer_class=Todolist_serilaizers

