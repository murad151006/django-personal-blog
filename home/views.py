from django.shortcuts import render, HttpResponse, redirect
from .models import ContactList
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def Home(request):
    return render(request, 'home/home.htm')


def About(request):
    return render(request, 'home/about.htm')


def Contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['Phone']
        email = request.POST['email']
        desc = request.POST['Description']
        print(name, phone, email, desc)

        if len(name)<2 or len(phone)<5 or len(email)<5 or len(desc)<10:
            messages.warning(request, 'Please submit the form with valid data')
        else:
            contact = ContactList(name=name, phone=phone, email=email, description=desc)
            contact.save()
            messages.success(request, 'You response has been submitted')
    return render(request, 'home/contact.htm')

def handleSignUp(request):
    if request.method =="POST":
        #get the parameters
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        #validation

        #create user
        myuser = User.objects.create_user(username, email, password1)
        myuser.email = email
        myuser.save()
        messages.success(request, "Success!")
        return redirect("/")
    else:
        return HttpResponse("Error")

def handlelogin(request):
    if request.method == "POST":
        #get the username and password
        loginusername = request.POST['username']
        passwordforsingle = request.POST['passwordforsingle']

        user = authenticate(username = loginusername, password=passwordforsingle)

        if user is not None:
            login(request, user)
            messages.success(request,"loggedin")
            return redirect('/')
        else: 
            messages.warning(request, "error")
    return HttpResponse ('sbchishdbc')

def handlelogout(request):
    logout(request)
    messages.success(request,"loggedout")
    return redirect('/')
    
