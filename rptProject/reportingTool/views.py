from django.shortcuts import render
from .forms import RptForms



# Create your views here.

def rpt_list(request):
    return render(request, "reportingTool/rpt_list.html")

def rpt_form(request):
    form = RptForms()
    return render(request, "reportingTool/rpt_form.html", {'form':form})

def rpt_delete(request):
    return