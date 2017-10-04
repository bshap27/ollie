from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^user/new/$', views.user_new, name='user_new'),
    url(r'^pet/new/$', views.pet_new, name='pet_new'),
]