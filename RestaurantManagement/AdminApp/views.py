from tkinter import Image

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from unicodedata import category

from AdminApp.models import CategoryDB, ProductDB, ServiceDB
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from WebApp.models import ContactDB
from django.contrib import messages


# Create your views here.
def index_page(request):
    categories=CategoryDB.objects.count()
    products=ProductDB.objects.count()
    return render(request,"index.html",{'categories':categories,'products':products})
def category_page(request):
    return render(request,"AddCategory.html")
def save_category(request):
    if request.method=="POST":
        name=request.POST.get('name')
        des=request.POST.get('description')
        img=request.FILES ['image']
        obj=CategoryDB(Name=name,Description=des,Image=img)
        obj.save()
        messages.success(request,"Category Saved Successfulyy...!")
        return redirect(category_page)
def display_category(request):
    data=CategoryDB.objects.all()
    return render(request,"DisplayCategory.html",{'data':data})
def edit_category(request,c_id):
    data=CategoryDB.objects.get(id=c_id)
    return render(request,"EditCategory.html",{'data':data})
def delete_category(request,c_id):
    category=CategoryDB.objects.filter(id=c_id)
    category.delete()
    messages.error(request, "Category Deleted Successfulyy...!")
    return redirect(display_category)
def update_category(request,c_id):
    if request.method=="POST":
        name=request.POST.get('name')
        des=request.POST.get('description')
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=CategoryDB.objects.get(id=c_id).Image
        CategoryDB.objects.filter(id=c_id).update(Name=name,Description=des,Image=file)
        messages.success(request, "Category updated Successfulyy...!")
        return redirect(display_category)
def product_page(request):
    cat=CategoryDB.objects.all()
    return render(request,"AddProduct.html",{'categories':cat})
def save_product(request):
    if request.method=="POST":
        cname=request.POST.get('category_name')
        pname=request.POST.get('product_name')
        des=request.POST.get('description')
        price=request.POST.get('price')
        img=request.FILES ['product_image']
        obj=ProductDB(Category_Name=cname, Product_Name=pname,Description=des,Price=price,Product_Image=img)
        obj.save()
        messages.success(request, "Product Saved Successfulyy...!")
        return redirect(product_page)
def display_product(request):
    pro=ProductDB.objects.all()
    return render(request,"DisplayProduct.html",{'pro':pro})
def delete_product(request,pro_id):
    product=ProductDB.objects.filter(id=pro_id)
    messages.error(request, "Product Deleted Successfulyy...!")
    product.delete()

    return redirect(display_product)
def edit_product(request,pro_id):
    cat=CategoryDB.objects.all()
    pro=ProductDB.objects.get(id=pro_id)
    return render(request,"EditProduct.html",{'pro':pro,'cat':cat})
def update_product(request,pro_id):
    if request.method=="POST":
        cname = request.POST.get('category_name')
        pname = request.POST.get('product_name')
        des = request.POST.get('description')
        price = request.POST.get('price')
        try:
            img = request.FILES['product_image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=ProductDB.objects.get(id=pro_id).Product_Image
        ProductDB.objects.filter(id=pro_id).update(
            Category_Name=cname,Product_Name=pname,Description=des,Price=price,Product_Image=file)
        messages.success(request, "Product updated Successfulyy...!")
        return redirect(display_product)
def admin_login_page(request):
    return render(request,"Admin_login_page.html")
def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pswd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            user=authenticate(username=un,password=pswd)
            if user is not None:
                request.session['username']=un
                request.session['password']=pswd
                login(request,user)
                return redirect(index_page)
            else:
                return redirect(admin_login_page)
        else:
            return redirect(admin_login_page)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)
def contact_data(request):
    data=ContactDB.objects.all()
    return render(request,"ContactData.html",{'data':data})
def delete_contact_data(request,cnt_id):
    contact=ContactDB.objects.filter(id=cnt_id)
    contact.delete()
    return redirect(contact_data)
def service_page(request):
    return render(request,"AddService.html")
def save_service(request):
    if request.method=="POST":
        s_name=request.POST.get('service_name')
        des=request.POST.get('description')
        obj=ServiceDB(Service_Name=s_name,Description=des)
        obj.save()
        return redirect(service_page)
def display_service(request):
    data=ServiceDB.objects.all()
    return render(request,"DisplayService.html",{'data':data})
def edit_service(request,s_id):
    data=ServiceDB.objects.get(id=s_id)
    return render(request,"EditService.html",{'data':data})
def delete_service(request,s_id):
    service=ServiceDB.objects.filter(id=s_id)
    service.delete()
    return redirect(display_service)
def update_service(request,s_id):
    if request.method=="POST":
        name=request.POST.get('service_name')
        des=request.POST.get('description')
        ServiceDBobjects.filter(id=s_id).update(Service_Name=name,Description=des)
        return redirect(display_category)