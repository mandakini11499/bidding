from django.shortcuts import render,redirect
from django.contrib import messages
from user.models import RegisterModel
from badmin.smsprocess import sendSMS

def adminCheck(request):
    uname=request.POST["t1"]
    pwd=request.POST["t2"]
    if uname == "admin" and pwd == "admin":
        return redirect("admin_home")
    else:
        messages.error(request,"Invalid Details")
        return redirect("admin_login")


def pendingReg(request):
    res=RegisterModel.objects.filter(status="pending")
    return render(request,"badmin_templates/pending_reg.html",{"data":res})


def approveReg(request):
    res=RegisterModel.objects.filter(status="approved")
    return render(request,"badmin_templates/approved_reg.html",{"data":res})


def declineReg(request):
    qs = RegisterModel.objects.filter(status="decline")
    return render(request, "badmin_templates/decline_reg.html", {"data": qs})


def approve(request):
    idno = request.POST["a1"]
    qs = RegisterModel.objects.filter(id=idno)
    name = ""
    cno = ""
    for x in qs:
        name = x.name
        cno = x.contact
    qs.update(status="approved")

    mess = "Hello Mr/Miss : " + name + ". Your Registration is Approved"
    x = sendSMS(str(cno), mess)
    print(x)
    return redirect('approved_reg')


def decline(request):
    idno = request.POST["a2"]
    qs = RegisterModel.objects.filter(id=idno)
    name = ""
    cno = ""
    for x in qs:
        name = x.name
        cno = x.contact
    qs.update(status="decline")

    mess = "Hello Mr/Miss : " + name + ". Your Registration is Declined"
    x = sendSMS(str(cno), mess)
    print(x)
    return redirect('decline_reg')


def logoutAdmin(request):
    return redirect("index")