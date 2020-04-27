from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [

    path('stocks/',views.index,name='index'),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('stocks/details/<str:id>/',views.details,name='details')


];