from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import product,add_item_done,rate_us
from datetime import datetime
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import  login_required
@login_required
def addactivity(request):
    if request.method=="POST":
        activity=request.POST['activity']
        dates=request.POST['dates']
        months=request.POST['months']
        years=request.POST['years']
        hours=request.POST['hours']
        mins=request.POST['mins']
        if activity!="" and dates!="" and months!="" and hours!="" and mins!="" and years!="":
            if dates.isdigit() and months.isdigit() and hours.isdigit() and mins.isdigit() and years.isdigit():
                if (int(dates)>31 or int(dates)<=0):
                    messages.info(request,"enter valid date")
                    return redirect('addactivity')
                elif int(dates)>29:
                    messages.info(request,"feb don't have "+dates+" days")
                    return redirect('addactivity')
                elif not((int(years)%400==0) or (int(years)%100!=0 and int(years)%4==0)) and int(dates)==29:
                    messages.info(request,"In "+str(years)+" feb has only 28 days")
                    return redirect('addactivity')
                elif (int(months) not in [1,3,5,7,8,10,12]) and int(dates)==31:
                    messages.info(request,months+" month contains only 30 days")
                    return redirect('addactivity')
                elif int(months)>12 or int(months)<=0:
                    messages.info(request,"enter valid month")
                    return redirect('addactivity')
                elif int(hours)>23 or int(hours)<0:
                    messages.info(request,"enter vaild hour")
                    return redirect('addactivity')
                elif int(mins)>59 or int(mins)<0:
                    messages.info(request,"enter valid minutes")
                    return redirect('addactivity')
                elif (int(years)<datetime.now().year):
                    messages.info(request,"update your year")
                    return redirect('addactivity')
                elif (int(months)<datetime.now().month) and int(years)==datetime.now().year:
                    messages.info(request,"update your month")
                    return redirect('addactivity')
                elif (int(dates)<datetime.now().day) and int(years)==datetime.now().year and int(months)==datetime.now().month:
                    messages.info(request,"update your day")
                    return redirect('addactivity')
                elif (int(hours)<datetime.now().hour) and int(years)==datetime.now().year and int(months)==datetime.now().month and int(dates)==datetime.now().day:
                    messages.info(request,"update your hour")
                    return redirect('addactivity')
                elif (int(mins)<datetime.now().minute) and int(years)==datetime.now().year and int(months)==datetime.now().month and int(dates)==datetime.now().day and int(hours)==datetime.now().minute:
                    messages.info(request,"update your minutes")
                    return redirect('addactivity')
                elif product.objects.filter(years=years,months=months,dates=dates,hours=hours,mins=mins).exists():
                    messages.info(request,"You have another task at that time")
                    return redirect('addactivity')
                elif len(activity.split())>20:
                    messages.info(request,"activity must be below 20 words")
                    return redirect('addactivity')
                else:
                    k=product(user=request.user,activity=activity,dates=dates,months=months,hours=hours,mins=mins,years=years)
                    k.save()
                    messages.info(request,"saved!")
                    return redirect('addactivity')
            else:
                messages.info(request,"Invalid date or time")
                return redirect('addactivity')
        else:
            messages.info(request,"please fill the details")
            return redirect('addactivity')

    else:
        return render(request,'addactivity.html',{'link' : 'http://127.0.0.1:8000/home/' , 'linkaddacivity' : 'http://127.0.0.1:8000/addactivity/','linktodonelist' : 'http://127.0.0.1:8000/donelist/', 'linktorateus' : 'http://127.0.0.1:8000/rateus/','linktoregister' : 'http://127.0.0.1:8000/accounts/register/','linktologin' : 'http://127.0.0.1:8000/accounts/login/','linktologout' : 'http://127.0.0.1:8000/logout/'})
@login_required
def home(request):
    tasks=product.objects.filter(user=request.user)
    search=request.GET.get('search')
    if search!="" and search is not None:
        tasks=tasks.filter(activity__icontains=search)
    if tasks.count()>1:
        sp="tasks"
    else:
        sp="task"
    return render(request,'home.html',{'tasks':tasks,'sp':sp ,'incomplete' : tasks.count(),'linktoaddactivity' : 'http://127.0.0.1:8000/addactivity/','linktodonelist' : 'http://127.0.0.1:8000/donelist/' , 'linktorateus' : 'http://127.0.0.1:8000/rateus/','linktoregister' : 'http://127.0.0.1:8000/accounts/register/','linktologin' : 'http://127.0.0.1:8000/accounts/login/', 'linktologout' : 'http://127.0.0.1:8000/logout/'})
@login_required
def donelist(request):
    tasks=add_item_done.objects.filter(user=request.user)
    search=request.GET.get('search')
    if search!="" and search is not None:
        tasks=tasks.filter(activity__icontains=search)
    if tasks.count()>1:
        sp="tasks"
    else:
        sp="task"
    return render(request,'donelist.html',{'sp':sp ,'incomplete' : tasks.count(), 'link' : 'http://127.0.0.1:8000/home/' , 'linktoaddactivity' : 'http://127.0.0.1:8000/addactivity/','linktodonelist' : 'http://127.0.0.1:8000/donelist/','tasks' : tasks ,'linktorateus' : 'http://127.0.0.1:8000/rateus/','linktoregister' : 'http://127.0.0.1:8000/register/','linktologin' : 'http://127.0.0.1:8000/login/'})
def rateus(request):
    if request.method=="POST":
        rating=request.POST['rating']
        description=request.POST['description']
        if rating!="" and description!="":
            if int(rating)>5 or int(rating)<1:
                messages.info(request,"rate us between 1-5")
                return redirect('rateus')
            else:
                r=rate_us(rating=rating,description=description)
                r.save()
                messages.info(request,"Thanks for your response")
                return redirect('rateus')
        else:
            messages.info(request,"please fill all the fileds")
            return redirect('rateus')
    else:
        return render(request,'settings.html',{ 'link' : 'http://127.0.0.1:8000/home/' , 'linktoaddactivity' : 'http://127.0.0.1:8000/addactivity/','linktodonelist' : 'http://127.0.0.1:8000/donelist/','linktorateus' : 'http://127.0.0.1:8000/rateus/','linktoregister' : 'http://127.0.0.1:8000/accounts/register/','linktologin' : 'http://127.0.0.1:8000/account/login/'})
def delete_item(request , item_id):
    product.objects.get(id=item_id).delete()
    return redirect('home')
@login_required
def additemdone(request,item_id):
    x=product.objects.get(id=item_id)
    if x.user==request.user:
        activity=x.activity
        dates=x.dates
        months=x.months
        years=x.years
        hours=x.hours
        mins=x.mins
        k=add_item_done(user=request.user,activity=activity,dates=dates,months=months,years=years,hours=hours,mins=mins)
        k.save()
        product.objects.get(id=item_id).delete()
        return redirect('home')
@login_required
def additemhome(request,item_id):
    x=add_item_done.objects.get(id=item_id)
    if x.user==request.user:
        activity=x.activity
        dates=x.dates
        months=x.months
        years=x.years
        hours=x.hours
        mins=x.mins
        k=product(user=request.user,activity=activity,dates=dates,months=months,years=years,hours=hours,mins=mins)
        k.save()
        add_item_done.objects.get(id=item_id).delete()
        return redirect('donelist')
def delete_item_done(request , item_id):
    add_item_done.objects.get(id=item_id).delete()
    return redirect('donelist')
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name=request.POST['first_name'] 
        last_name=request.POST['last_name']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if username!="" and password1!="" and password2!="" and first_name!="":
            if password1!=password2:
                messages.info(request,"password didn't match")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            else:
                r=User.objects.create_user(username=username,first_name=first_name,password=password1,last_name=last_name)
                r.save()
                messages.info(request,"Saved! You can login now ")
                return redirect('register')
        else: 
            messages.info(request,'fill required fields')
            return redirect('register')
    else:
        return render(request,'register.html',{ 'link' : 'http://127.0.0.1:8000/home/','linktoaddactivity' : 'http://127.0.0.1:8000/addactivity/','linktodonelist' : 'http://127.0.0.1:8000/donelist/' , 'linktorateus' : 'http://127.0.0.1:8000/rateus/','linktoregister' : 'http://127.0.0.1:8000/accounts/register/','linktologin' : 'http://127.0.0.1:8000/accounts/login/'})  
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        if username=="" and password=="": 
            messages.info(request,"please fill required fileds")
            return redirect('login')
        else:
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                messages.info(request,"Logged in successfully!!")
                return redirect('home')
            else:
                messages.info(request,"invalid username or password")
                return redirect('login')
    else:
        return render(request,'login.html',{ 'link' : 'http://127.0.0.1:8000/home/' ,'linktoaddactivity' : 'http://127.0.0.1:8000/addactivity/','linktodonelist' : 'http://127.0.0.1:8000/donelist/', 'linktorateus' : 'http://127.0.0.1:8000/rateus/','linktoregister' : 'http://127.0.0.1:8000/accounts/register/','linktologin' : 'http://127.0.0.1:8000/login/'})
def logout(request):
    auth.logout(request)
    return render(request,'home.html',{'linktoaddactivity' : 'http://127.0.0.1:8000/addactivity/','linktodonelist' : 'http://127.0.0.1:8000/donelist/' , 'linktorateus' : 'http://127.0.0.1:8000/rateus/','linktoregister' : 'http://127.0.0.1:8000/accounts/register/','linktologin' : 'http://127.0.0.1:8000/accounts/login/'})