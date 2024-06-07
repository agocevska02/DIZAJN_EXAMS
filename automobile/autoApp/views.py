from django.shortcuts import render, redirect

from autoApp import models
from autoApp.forms import FixForm


# Create your views here.
def index(request):
    return render(request, "index.html")


def save_fix(request):
    fixes = models.Fix.objects.filter(user=request.user).filter(automobile__type__iexact="sedan").all()
    if request.method == "POST":
        fixForms = FixForm(request.POST, request.FILES)
        if fixForms.is_valid():
            fixForms.instance.user = request.user
            fixForms.save()
            return redirect("repairs")
    else:
        fixForms = FixForm()
    return render(request, "repairs.html", {"form": fixForms, "fixes": fixes})


def edit_fix(request, id):
    fix = models.Fix.objects.filter(id=id).get()
    if request.method == "POST":
        fixForms = FixForm(request.POST, request.FILES, instance=fix)
        if fixForms.is_valid():
            fixForms.instance.user = request.user
            fixForms.save()
            return redirect("repairs")
    else:
        fixForms = FixForm(instance=fix)
    return render(request, "edit_fix.html", {"form": fixForms})


def delete_fix(request, id):
    fix = models.Fix.objects.filter(id=id).get()
    if request.method == "POST":
        fix.delete()
        return redirect("repairs")
    return render(request, "delete_fix.html", {"fix": fix})
