from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from .models import Dealer, Item


# Create your views here.
def dealerlogin(request):
    return render(request, 'dealerlogin.html')


def dealersignin(request):
    return render(request, 'dealersignin.html')


def checkdlogin(request):
    email = request.POST.get('email')
    dpassword = request.POST.get('password')

    flag = Dealer.objects.filter((Q(email=email) | Q(username=email)) & Q(password=dpassword))
    if flag:
        dealer = Dealer.objects.get(password=dpassword)
        uname = dealer.username
        id = dealer.id
        return render(request, 'dealermenu.html', {'uname': uname, 'id': id})
    else:
        # return HttpResponse("Login Failed")
        msg = "Wrong Credentials"
        return render(request, 'dealerlogin.html', {'msg1': msg})


def creatduser(request):
    if request.method == 'POST':
        fname = request.POST["fname"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        password = request.POST["password"]
        dealer = Dealer(Fullname=fname, email=email, phno=phno, username=uname, password=password)
        Dealer.save(dealer)
        msg = "Registration is Successful"
        subject = 'Thank you for registering to our site'
        message = 'HEY ' + fname + ' You are now successfully registered with us. Your Password is secure now!'
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, [email])
        return render(request, 'dealerlogin.html', {'msg': msg})


def dforgetpage(request):
    return render(request, 'dealerforgetpage.html')


def dforgetpassword(request):
    email = request.POST["email"]
    phno = request.POST["phno"]

    flag = Dealer.objects.filter(Q(email=email) & Q(phno=phno))

    if flag:
        dealer = Dealer.objects.get(email=email, phno=phno)
        password = dealer.password
        msg = "Your password is "
        return render(request, 'dealerforgetpage.html', {'msg': msg, 'password': password})
    else:
        msg = "User not found"
        return render(request, 'dealerforgetpage.html', {'msg1': msg})


def menu(request):
    item = Item.objects.all()
    count = Item.objects.count()
    return render(request, 'dealermenu.html', {'itemdata': item, 'count': count})


def add(request):
    return render(request, 'additem.html')



def additem(request):
    if request.method == 'POST':
        name = request.POST['name']
        offer = request.POST['offer']
        price = request.POST['price']
        # image = request.FILES['image']
        # promoted = request.POST['promoted']
        i = Item(name=name, offer=offer, price=price)
        Item.save(i)
        msg = 'Item added to the menu succesfully'
        return render(request, 'dealermenu.html', {'msg': msg})
