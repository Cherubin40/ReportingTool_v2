from django.urls import path
from . import views

urlpatterns = [
    path('', views.rpt_form), #localhost:p/reportingTool/
    path('list/', views.rpt_list) #localhost:p/reportingTool/list
]
