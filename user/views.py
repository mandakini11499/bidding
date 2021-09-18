from django.contrib import messages
from django.shortcuts import render,redirect

# Create your views here.
from user.models import RegisterModel, ProductModel,BidtableModel


def register(request):
    name = request.POST["s1"]
    contact = request.POST["s2"]
    email = request.POST["s3"]
    password = request.POST["s4"]
    status = "pending"
    RegisterModel(name=name, contact=contact, email=email, password=password, status=status).save()
    messages.success(request, "Registration Need to Approve By Admin")
    return redirect("buyer_seller")


def userLogin(request):
    con=request.POST["b1"]
    pwd=request.POST["b2"]
    try:
        res=RegisterModel.objects.get(contact=con,password=pwd)
        if res.status=="approved":
            request.session['username']=res.name
            request.session['uid']=res.id
            return render(request,"user_templates/user_home.html")
        elif res.status=="pending":
            messages.error(request, "Your Registration in Pending")
            return redirect("buyer_seller")

        else:
          messages.error(request, "Your Registration in Declined")
          return redirect("buyer_seller")

    except RegisterModel.DoesNotExist:
         messages.error(request, "Invalid User")
         return redirect("buyer_seller")


def user_logout(request):
    del request.session["username"]
    return redirect('index')


def saveProduct(request):
    pno=request.POST["p1"]
    pna=request.POST["p2"]
    pinfo=request.POST["p3"]
    pimage=request.FILES["p4"]
    price=request.POST["p5"]
    status="bidding"
    uid=request.session["uid"]
    ProductModel(pno=pno,pname=pna,pinfo=pinfo,image=pimage,bprice=price,status=status,uid=uid).save()
    qs = ProductModel.objects.all()
    return render(request, "user_templates/sell_product.html", {"data": qs})



def sellProduct(request):
    qs=ProductModel.objects.all()
    return render(request,"user_templates/sell_product.html",{"data":qs})


def buyProduct(request):
    qs = ProductModel.objects.all()
    return render(request,"user_templates/buy_product.html", dict(data=qs))


def saveBT(request):
    pno=request.POST['t1']
    amt=request.POST['t2']
    uid=request.session["uid"]
    BidtableModel(pno_id=pno,amount=amt,uid_id=uid).save()
    qs=ProductModel.objects.all()
    return render(request, "user_templates/sell_product.html",{"data":qs})

from django.db.models import Count
def bData(request):
    qs=BidtableModel.objects.all()
    return render(request,"user_templates/bdata.html",{"data":qs})
