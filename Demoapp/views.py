from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from Demoapp.models import Admindb, Addcategorydb, Productdetailsdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def samplepage(request):
    return render(request, "Sample.html")
def Adminpage(req):
    return render(req, "Addadmin.html")
def Adminsave(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        mb = request.POST.get('mobile')
        un = request.POST.get('uname')
        pw = request.POST.get('pswrd')
        img = request.FILES['image']
        obj = Admindb(Name=na, Email=em, Mobile=mb, Username=un, Password=pw, Image=img)
        obj.save()
        return redirect(Adminpage)

def Displayadmin(req):
    data = Admindb.objects.all()
    return render(req, "Displayadmin.html", {'data': data})
def Editadmin(req, dataid):
    data = Admindb.objects.get(id=dataid)
    print(data)
    return render(req, "Editadmin.html", {'data':data})

def Updateadmin(request, dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        mb = request.POST.get('mobile')
        un = request.POST.get('uname')
        pw = request.POST.get('pswrd')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = Admindb.objects.get(id=dataid).Image
        Admindb.objects.filter(id=dataid).update(Name=na, Email=em, Mobile=mb, Username=un, Password=pw, Image=file)
        return redirect(Displayadmin)

def Deleteadmin(req, dataid):
    data = Admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(Displayadmin)

def Addcategory(request):
    return render(request, "Addcategory.html")

def Categorysave(req):
    if req.method == "POST":
        ct = req.POST.get('catgry')
        ds = req.POST.get('dscrptn')
        img = req.FILES['image']
        obj = Addcategorydb(Category=ct, Description=ds, Image=img)
        obj.save()
        return redirect(Addcategory)
def DisplayCategory(request):
    data = Addcategorydb.objects.all()
    return render(request, "Displaycategory.html", {'data': data})
def Editcategory(req, dataid):
    data = Addcategorydb.objects.get(id=dataid)
    print(data)
    return render(req, "Editcategory.html", {'data': data})
def Updatecategory(req, dataid):
    if req.method == "POST":
        ct = req.POST.get('catgry')
        ds = req.POST.get('dscrptn')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = Addcategorydb.objects.get(id=dataid).Image
        Addcategorydb.objects.filter(id=dataid).update(Category=ct, Description=ds, Image=file)
        return redirect(DisplayCategory)
def Deletecategory(req, dataid):
    data = Addcategorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(DisplayCategory)

def Addproduct(request):
    data = Addcategorydb.objects.all()
    return render(request, "Addproduct.html", {'data': data})
def Productsave(req):
    if req.method == "POST":
        ct = req.POST.get('category')
        pn = req.POST.get('product')
        pr = req.POST.get('price')
        qy = req.POST.get('quantity')
        ds = req.POST.get('dscrptn')
        img = req.FILES['image']
        obj = Productdetailsdb(Category=ct, ProductName=pn, Price=pr, Quantity=qy, Description=ds, Image=img)
        obj.save()
        return redirect(Addproduct)
def Displayproduct(request):
    data = Productdetailsdb.objects.all()
    return render(request, "Displayproduct.html", {'data': data})
def Editproduct(req, dataid):
    data = Productdetailsdb.objects.get(id=dataid)
    da = Addcategorydb.objects.all()
    print(data)
    return render(req, "Editproduct.html", {'data': data, 'da': da})
def Updateproduct(req, dataid):
    if req.method == "POST":
        ct = req.POST.get('category')
        pn = req.POST.get('product')
        pr = req.POST.get('price')
        qy = req.POST.get('quantity')
        ds = req.POST.get('dscrptn')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = Productdetailsdb.objects.get(id=dataid).Image
        Productdetailsdb.objects.filter(id=dataid).update(Category=ct, ProductName=pn, Price=pr, Quantity=qy, Description=ds, Image=file)
        return redirect(Displayproduct)
def Deleteproduct(req, dataid):
    data = Productdetailsdb.objects.filter(id=dataid)
    data.delete()
    return redirect(Displayproduct)
def Adminloginpage(request):
    return render(request, "Adminlogin.html")
def Adminlogin(req):
    if req.method=="POST":
        username_r = req.POST.get('username')
        password_r = req.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(req, user)
                req.session['username']=username_r
                req.session['password']=password_r
                return redirect(samplepage)
            else:
                return redirect(Adminloginpage)
        else:
            return redirect(Adminloginpage)
def Adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(Adminloginpage)

