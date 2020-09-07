from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RptForms
from .models import Patient



# Create your views here.

def rpt_list(request):
    context = {'patient_list': Patient.objects.all()}
    return render(request, "reportingTool/rpt_list.html", context)

@login_required
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
        return redirect('patient_list')

def rpt_delete(request, id):
    patient = Patient.objects.get(pk=id)
    patient.delete()
    return redirect('patient_list')


# Authentification

#def loginView(request):
#    return render(request, "reportingTool/login.html")

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "reportingTool/register.html", {'form': form})