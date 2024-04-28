from rest_framework import serializers

from base.models import Users
from base.models import Todolist




class User_serilaizers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=Users
        fields=['id','name','mobile_no','password']

class Todolist_serilaizers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=Todolist
        fields=['id','user_id','title','date','time','tags','status']


