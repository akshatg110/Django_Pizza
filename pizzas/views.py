from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import PizzaModel,CustomerModel,OrderModel
from django.contrib.auth.models import User

# Create your views here.
def adminloginview(request):
    return render(request,"pizzaapp/adminlogin.html")
def authenticateadmin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    #user exit
    if user is not None and user.username=="admin":
        login(request,user)
        return redirect('adminhomepage')

    #user doesnot exit
    if user is None:
        messages.add_message(request,messages.ERROR,"invalid credentials")
        return redirect('adminloginpage')

def adminhomepageview(request):
    context = {'pizzas' : PizzaModel.objects.all()}
    return render(request,"pizzaapp/welcome.html",context)
def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')
def addpizza(request):
    name = request.POST['pizza']
    price = request.POST['price']
    PizzaModel(name = name,price = price).save()
    return redirect('adminhomepage')
def deletepizza(request,pizzapk):
    PizzaModel.objects.filter(id=pizzapk).delete()
    return redirect('adminhomepage')
def homepageview(request):
    return render(request,"pizzaapp/homepage.html")
def signupuser(request):
    username = request.POST['username']
    password = request.POST['password']
    phoneno = request.POST['phonenumber']
    #already exist
    if User.objects.filter(username = username).exists():
        messages.add_message(request,messages.ERROR,"user already exist")
        return redirect('homepage')
    #new user
    User.objects.create_user(username = username, password = password).save()
    lastobject = len(User.objects.all())-1
    CustomerModel(userid = User.objects.all()[int(lastobject)].id,phoneno = phoneno).save()
    messages.add_message(request,messages.ERROR,"user succesfully created")
    return redirect('homepage')
def userloginview(request):
    return render(request,"pizzaapp/userlogin.html")
def userauthenticate(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect('customerpage')
    if user is None:
        messages.add_message(request,messages.ERROR,"invalid credentials")
        return redirect('userloginpage')
def customerwelcomeview(request):
    if not request.user.is_authenticated:
        return redirect('customerpage')

    username = request.user.username
    context = {'username' : username, 'pizzas' : PizzaModel.objects.all()}
    return render(request,'pizzaapp/customerwelcomeview.html',context)

def userlogout(request):
    logout(request)
    return redirect('homepage')

def placeorder(request):
    username = request.user.username
    
    

    address = request.POST['address']
    ordereditems = ""
    for pizza in PizzaModel.objects.all():
        pizzaid = pizza.id
        name = pizza.name
        price = pizza.price
        quantity = request.POST.get(str(pizzaid)," ")
        if str(quantity)!="0" and str(quantity)!=" ":
            ordereditems = ordereditems + name + " "+"price"+ str(int(price)*int(quantity))+" "+"quantity: "+quantity+" "

    OrderModel(username = username,phoneno = address,address = address, orderitems =  ordereditems).save()
    messages.add_message(request,messages.ERROR,"Order placed Successfully")
    return redirect('customerpage')
def userorders(request):
    orders = OrderModel.objects.filter(username= request.user.username)
    context = {'orders' : orders}
    return render(request,'pizzaapp/userorders.html',context)
def adminorder(request):
    orders = OrderModel.objects.all()
    context = {'orders' : orders}
    return render(request,'pizzaapp/adminorderrequest.html',context)
def acceptorder(request,orderpk):
    order = OrderModel.objects.filter(id = orderpk)[0]
    order.status="Accepted"
    order.save()
    return redirect(request.META['HTTP_REFERER'])
def declineorder(request,orderpk):
    order = OrderModel.objects.filter(id = orderpk)[0]
    order.status="Declined"
    order.save()
    return redirect(request.META['HTTP_REFERER'])
