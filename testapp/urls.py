from django.conf.urls import url
from testapp import views

urlpatterns = [
    url('', views.index, name='index'),
]
