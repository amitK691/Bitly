from django.urls import path,include
from crul import views

urlpatterns = [

	path('crul/',views.crul_check,name ='crul'),

]