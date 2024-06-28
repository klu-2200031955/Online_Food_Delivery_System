from django.db.models import Q
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from .models import Customer, Address, Card, Upi


# Create your views here.
def customerlogin(request):
    return render(request, 'customerlogin.html')


def customerhome(request):
    # uname = request.session.get("uname")
    # m = Customer.objects.filter(Q(email=uname) | Q(username=uname))
    # username = m.username
    # return render(request, 'customerhome.html', {'uname': username})
    return render(request, 'customerhome.html')


def customersignin(request):
    return render(request, 'customersignin.html')


def createcuser(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        password = request.POST["pass"]
        customer = Customer(Fullname=fname, email=email, phno=phno, username=uname, password=password)
        Customer.save(customer)
        msg = "Registration is Successful"
        subject = 'Thank you for registering to our site'
        message = 'HEY ' + uname + ' You are now successfully registered with us. Your Password is secure now!'
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, [email])
        return render(request, 'customerlogin.html', {'msg1': msg})


def checkclogin(request):
    email = request.POST.get('email')
    cpassword = request.POST.get('password')

    flag = Customer.objects.filter((Q(email=email) | Q(username=email)) & Q(password=cpassword))
    if flag:
        customer = Customer.objects.get(password=cpassword)
        request.session["username"] = customer.username
        request.session["fname"] = customer.Fullname
        request.session["email"] = customer.email
        request.session["phno"] = customer.phno
        return render(request, 'customerhome.html', {'uname': customer.username})
    else:
        # return HttpResponse("Login Failed")
        msg = "Wrong Credentials"
        return render(request, 'customerlogin.html', {'msg': msg})


def cforgetpage(request):
    return render(request, 'customerforgetpage.html')


def cforgetpassword(request):
    email = request.POST["email"]
    phno = request.POST["phno"]
    flag = Customer.objects.filter(Q(email=email) & Q(phno=phno))

    if flag:
        customer = Customer.objects.get(email=email, phno=phno)
        password = customer.password
        msg = "Your password is "
        return render(request, 'customerforgetpage.html', {'msg': msg, 'password': password})
    else:
        msg = "User not found"
        return render(request, 'customerforgetpage.html', {'msg1': msg})


def spaymentpage(request):
    uname = request.session['username']
    fname = request.session['fname']
    email = request.session['email']
    phno = request.session['phno']
    if request.method == 'POST':
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        pcode = request.POST['pcode']
        add = Address(username=uname, fullname=fname, email=email, address=address, city=city, state=state, phno=phno,
                      pincode=pcode)
        Address.save(add)
        if request.POST['type'] == 'dcard':
            return render(request, 'paymentpage2.html')
        elif request.POST['type'] == 'ccard':
            return render(request, 'paymentpage3.html')
        elif request.POST['type'] == 'upi':
            return render(request, 'paymentpage4.html')
        elif request.POST['type'] == 'cod':
            return HttpResponse('Order is Placed')
        else:
            msg = 'Some Data given is Wrong Please Verify it'
            return render(request, 'paymentpage1.html', {'msg': msg})


def npaymentpage(request):
    name = request.session['fname']
    email = request.session['email']
    return render(request, 'paymentpage1.html', {'fname': name, 'email': email})


def createcard(request):
    uname = request.session['username']
    if request.method == 'POST':
        chname = request.POST['ncard']
        cnumber = request.POST['nnumber']
        expdate = request.POST['edate']
        cvv = request.POST['cvv']
        card = Card(username=uname, chname=chname, cnumber=cnumber, expdate=expdate, cvv=cvv)
        Card.save(card)
        return render(request, 'customerhome.html', {'uname': uname})


def cupi(request):
    uname = request.session['username']
    if request.method == 'POST':
        uid = request.POST['uid']
        upi = Upi(username=uname, upi=uid)
        Upi.save(upi)
        return HttpResponse('Order is Placed')