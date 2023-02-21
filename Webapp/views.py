from django.shortcuts import render, redirect
from Demoapp.models import Addcategorydb, Productdetailsdb
from Webapp.models import Customerdetails, CheckOutdetails, Contactus
from django.contrib import messages

# Create your views here.
def webpage(request):
    data = Addcategorydb.objects.all()
    da = Productdetailsdb.objects.all()
    return render(request, "Webpage.html",{'data': data, 'da':da})
def Aboutuspage(req):
    return render(req, "AboutUs.html")
def Contactuspage(req):
    return render(req, "ContactUs.html")
def Productdisplay(req, itemCatg):
    data = Addcategorydb.objects.all()
    catg = itemCatg.upper()
    products = Productdetailsdb.objects.filter(Category=itemCatg)
    context = {
            'products': products,
            'catg': catg,
            'data': data
    }
    return render(req, "ProductDisplay.html", context)

def Singleproduct(req,dataid):
    da = Addcategorydb.objects.all()
    data = Productdetailsdb.objects.get(id=dataid)
    return render(req, "SingleProduct.html", {'data':data, 'da':da})

def Addtocart(request, dataid):
    da = Addcategorydb.objects.all()
    data = Productdetailsdb.objects.get(id=dataid)
    return render(request, "AddToCart.html",{'data':data})

def CheckOut(req):
    data = Addcategorydb.objects.all()
    return render(req, "Checkout.html", {'data': data})

def Checkoutsave(req):
    if req.method == "POST":
        fn = req.POST.get('fname')
        ln = req.POST.get('lname')
        ad = req.POST.get('address')
        ct = req.POST.get('tcity')
        ps = req.POST.get('pst')
        ph = req.POST.get('phn')
        em = req.POST.get('email')
        obj = CheckOutdetails(Firstname=fn, Lastname=ln, Address=ad, City=ct, Postcode=ps, Phone=ph, Email=em)
        obj.save()
        messages.success(req,"Order Placed Succesfully")
        return redirect(webpage)

def Login(req):
    return render(req, "LogInPage.html")

def Loginsave(request):
    if request.method == "POST":
        na = request.POST.get('username')
        em = request.POST.get('email')
        pswd = request.POST.get('password')
        cfpswd = request.POST.get('cfpassword')
        if pswd==cfpswd:
            obj = Customerdetails(Username=na, Email=em, Password=pswd, ConfirmPassword=cfpswd)
            obj.save()
            messages.success(request,"Registerd Succesfully")
            return redirect(Login)
        else:

            return render(request,"LogInPage.html",{'msg':"Sorry Password Not Matched"})

def Customerlogin(request):
    if request.method=="POST":
        Username_r=request.POST.get("username")
        Password_r=request.POST.get("password")
        if Customerdetails.objects.filter(Username=Username_r, Password=Password_r).exists():
            request.session['username']=Username_r
            request.session['password']=Password_r
            messages.success(request,"Login Successfully")

            return redirect(webpage)
        else:
            messages.error(request,"Invalid User")
            return render(request,'LogInPage.html')

def Customerlogout(req):
    del req.session['username']
    del req.session['password']
    return redirect(Login)


def Contactsave(req):
    if req.method == "POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        sb = req.POST.get('subject')
        ms = req.POST.get('message')
        obj = Contactus(Name=na, Email=em, Subject=sb, Message=ms)
        obj.save()
        return redirect(Contactuspage)