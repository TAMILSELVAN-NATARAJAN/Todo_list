from django.urls import path ,include
from rest_framework import routers

from base.views import todolist_viewsets
from base.views import user_viewsets



router=routers.DefaultRouter()

router.register('User',user_viewsets)
router.register('Todolist',todolist_viewsets)

# router('Users',)

urlpatterns = [
    path('',include(router.urls)),
]