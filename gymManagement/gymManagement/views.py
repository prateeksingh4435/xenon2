from django.shortcuts import HttpResponse ,redirect,render 
from django.http import HttpResponseForbidden
from django.shortcuts import HttpResponse,render,redirect
from management.models import contact,signupdata
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    messages.success(request,'logout successfully')
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def classes(request):
    return render(request ,'classes.html')

def contacts(request):
    if request.method=="POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')

        desc = request.POST.get('textarea')
        alldata = contact(firstname = firstname , lastname =lastname,email=email,concern=desc)
        alldata.save()


    return render(request,'contact.html',)
   

def pricing(request):
    return render(request, 'pricing.html')


def signup(request):
    if request.method=="POST":
        firstname  = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username  = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirmpassword')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
                return redirect('signup')
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already used")
                return redirect('signup')
            user = signupdata(firstname = firstname ,lastname = lastname , email= email,username = username,password1=password1,password2 =password2)
            user.save()
            my_user = User.objects.create_user(username=username, password=password1)
            my_user.first_name = firstname
            my_user.last_name = lastname
            my_user.email = email

            my_user.save()
            messages.success(request, 'Sign-up successful')
        else:
            messages.error(request,'Password and Confirm Password Not Match')


    return render(request,'signup.html')


def userlogin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username= username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'Login-successfully')
            return redirect('afterlogin')
        else:
            messages.error(request,'Invalid username and password')

    return render(request,'userlogin.html')




@login_required(login_url='userlogin')
def afterlogin(request):
    if  request.user.is_authenticated:
        return render(request, 'afterlogin.html')
    
    

def logoutpage(request):
    logout(request)
    messages.error(request,'logout successfully')
    
    return redirect('index')