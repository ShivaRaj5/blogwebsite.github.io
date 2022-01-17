from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render(request,'home/home.html')
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<3:
            messages.error(request,"Please fill the from correctly")
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"Your query has been submitted. We will get back to you soon!")
    return render(request,'home/contact.html')
def about(request):
    return render(request,'home/about.html')
def search(request):
    query=request.GET['query']
    if len(query)>100 or len(query)==0:
        allPosts=Post.objects.none()
    else:
        allPostsTitle=Post.objects.filter(title__icontains=query)
        allPostsContent=Post.objects.filter(content__icontains=query)
        allPosts=allPostsTitle.union(allPostsContent)
    if allPosts.count()==0:
        messages.warning(request,"You didn't add any query or your query didn't match any of the posts or your query is too long.")
    params={'allPosts':allPosts,'query':query}
    return render(request,'home/search.html',params)
def handleSignup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if len(username)>20:
            messages.error(request,"Length of the username is too long.")
            return redirect('home')
        if not username.isalnum():
            messages.error(request,"Username should only contain letters and numbers.")
            return redirect('home')
        if password!=cpassword:
            messages.error(request,"Passwords do not match.")
            return redirect('home')
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your account has been created successfully.")
        return redirect('home')
    else:
        return HttpResponse("404 not found")
def handleLogin(request):
    if request.method=='POST':
        username=request.POST['loginusername']
        password=request.POST['loginpassword']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have successfully logged in.")
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials! Please try again.")
            return redirect('home')
    return HttpResponse("404 not found")
def handleLogout(request):
    logout(request)
    messages.success(request,"You have been successfully logged out!")
    return redirect('home')
