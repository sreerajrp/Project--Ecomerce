from django.shortcuts import render, redirect
from AdminApp.models import CategoryDB, ProductDB, ServiceDB
from WebApp.models import ContactDB, SignupDB, CartDB, OrderDB
from django.contrib import messages



# Create your views here.
def home_page(request):
    Categories=CategoryDB.objects.all()
    cart_total = CartDB.objects.filter(Username=request.session['Username'])
    x=cart_total.count()
    return render(request,"Home.html",{'Categories':Categories, 'x': x})

def about_page(request):
    Categories=CategoryDB.objects.all()
    cart_total = CartDB.objects.filter(Username=request.session['Username'])
    x = cart_total.count()
    return render(request,"About.html",{'Categories':Categories,'x': x})

def product_page(request):
    Products=ProductDB.objects.all()
    Categories = CategoryDB.objects.all()
    cart_total = CartDB.objects.filter(Username=request.session['Username'])
    x = cart_total.count()
    return render(request,"Products.html",{'Products':Products,'Categories':Categories,'x':x})

def services(request):
    Categories =CategoryDB.objects.all()
    Services=ServiceDB.objects.all()
    cart_total = CartDB.objects.filter(Username=request.session['Username'])
    x = cart_total.count()
    return render(request, "Services.html", {'Categories': Categories,'Services':Services,'x':x})

def contact(request):
    Categories = CategoryDB.objects.all()
    cart_total = CartDB.objects.filter(Username=request.session['Username'])
    x = cart_total.count()
    return render(request, "Contact.html", {'Categories': Categories,'x':x})

def save_contact_details(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        sub=request.POST.get('subject')
        msg=request.POST.get('message')
        obj = ContactDB(Name=name, Email=email,Subject=sub,Message=msg)
        obj.save()
        messages.success(request, "Submited Sucessfully")
        return redirect(contact)

def filtered_items(request,cat_name):
    Categories = CategoryDB.objects.all()
    data=ProductDB.objects.filter(Category_Name=cat_name)
    cart_total = CartDB.objects.filter(Username=request.session['Username'])
    x = cart_total.count()
    return render(request, "Filtered_items.html",{'data':data,'Categories':Categories,'x':x})

def single_item(request,item_id):
    product=ProductDB.objects.get(id=item_id)
    Categories = CategoryDB.objects.all()
    cart_total = CartDB.objects.filter(Username=request.session['Username'])
    x = cart_total.count()
    return render(request,"Single_item.html",{'product':product,'Categories':Categories,'x':x})

def sign_in(request):
    return render(request,"Sign_In.html")

def sign_up(request):
    return render(request,"Sign_Up.html")

def save_signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        email=request.POST.get('email')
        obj=SignupDB(Username=username,Password=pass1,Confirm_Password=pass2,Email=email)
        obj.save()
        messages.success(request,"Registered Sucessfully")
        return redirect(sign_in)

def user_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pswd=request.POST.get('pass1')
        if SignupDB.objects.filter(Username=un,Password=pswd ).exists():
            request.session['Username']=un
            request.session['Password']=pswd
            messages.success(request, "Welcome")
            return redirect(home_page)
        else:
            messages.warning(request, "Failed to login")
            return redirect(sign_in)
    else:
        messages.warning(request, "")
        return redirect(sign_in)
def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(sign_in)

def save_cart(request):
    if request.method=="POST":
        username=request.POST.get('username')
        product_name=request.POST.get('prod_name')
        quantity=request.POST.get('quantity')
        price=request.POST.get('price')
        total_price=request.POST.get('total')
        try:
            x=ProductDB.objects.get(Product_Name=product_name)
            img = x.Product_Image
        except ProductDB.DoesNotExist:
            img = None
        obj = CartDB(Username=username,Products=product_name,Quantity=quantity,Price=price,Total_Price=total_price,Prod_Image=img)
        obj.save()
        return redirect(home_page)
def cart_page(request):
    sub_total=0
    shipping_amount=0
    total_amount=0
    Categories = CategoryDB.objects.all()
    cart = CartDB.objects.filter(Username=request.session['Username'])
    for i in cart:
        sub_total+=i.Total_Price
        if sub_total>500:
            shipping_amount=50
        else:
            shipping_amount=100
        total_amount=sub_total+shipping_amount
        cart_total = CartDB.objects.filter(Username=request.session['Username'])
        x = cart_total.count()
    return render(request,"Cart.html",{'cart':cart,'sub_total':sub_total,'shipping_amount':shipping_amount,'total_amount':total_amount,'x':x,'Categories':Categories })
def delete_cart(request,cart_id):
    cart=CartDB.objects.filter(id=cart_id)
    cart.delete()
    return redirect(cart_page)
def checkout_page(request):
    sub_total = 0
    shipping_amount = 0
    total_amount = 0
    Categories = CategoryDB.objects.all()
    cart = CartDB.objects.filter(Username=request.session['Username'])
    for i in cart:
        sub_total += i.Total_Price
        if sub_total > 500:
            shipping_amount = 50
        else:
            shipping_amount = 100
        total_amount = sub_total + shipping_amount
        cart_count = CartDB.objects.count()
    return render(request, "Checkout.html", {'cart': cart, 'sub_total': sub_total, 'shipping_amount': shipping_amount,
                                         'total_amount': total_amount,'cart_count': cart_count, 'Categories':Categories })
def save_checkout(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        place=request.POST.get('place')
        address=request.POST.get('address')
        mobile=request.POST.get('mobile')
        state = request.POST.get('state')
        pincode=request.POST.get('pincode')
        total_price=request.POST.get('amount')
        message=request.POST.get('message')
        obj = OrderDB(Name=name, Email=email,Place=place,Address=address,Mobile=mobile,State=state,Pin=pincode,TotalPrice=total_price,Message=message)
        obj.save()
        return redirect(payment_page)
def payment_page(request):
    username = request.session['Username']
    sub_total = 0
    shipping_amount = 0
    total_amount = 0
    Categories = CategoryDB.objects.all()
    cart = CartDB.objects.filter(Username=request.session['Username'])
    for i in cart:
        sub_total += i.Total_Price
        if sub_total > 500:
            shipping_amount = 50
        else:
            shipping_amount = 100
        total_amount = sub_total + shipping_amount
        cart_total = CartDB.objects.filter(Username=request.session['Username'])
        x = cart_total.count()
    return render(request, "Payment.html", {'username':username,'cart': cart, 'sub_total': sub_total, 'shipping_amount': shipping_amount,
                                         'total_amount': total_amount, 'x': x, 'Categories':Categories})



