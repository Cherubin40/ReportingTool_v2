from django.shortcuts import render, redirect
from .forms import RptForms
from .models import Patient



# Create your views here.

def rpt_list(request):
    context = {'patient_list': Patient.objects.all()}
    return render(request, "reportingTool/rpt_list.html", context)

def rpt_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = RptForms()
        else:
            patient = Patient.objects.get(pk=id)
            form = RptForms(instance=patient)
        return render(request, "reportingTool/rpt_form.html", {'form':form})
    
    else:
        if id == 0:
            form = RptForms(request.POST)
        else:
            patient = Patient.objects.get(pk=id)
            form = RptForms(request.POST, instance=patient)
        if form.is_valid():
            form.save()
        return redirect('/reportingTool/list/')

def rpt_delete(request, id):
    patient = Patient.objects.get(pk=id)
    patient.delete()
    return redirect('/reportingTool/list/')