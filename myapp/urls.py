from django.urls import path,include
from . import views

from rest_framework import routers
from .views import UserViewApi
router =routers.DefaultRouter()
router.register('usersapi', UserViewApi)
#Github@0786
urlpatterns=[
    path('test1/',views.test),
    path('dform/',views.dform_text),
    path('adduser/',views.add_user, name='adduser'),
    path('form_save_user/',views.form_save_user, name='form_save_user'),
    path('api/', include(router.urls)),
]
