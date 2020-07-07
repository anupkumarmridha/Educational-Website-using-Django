from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from blog.models import Post
# Create your views here.
def home(request):
    return render(request, 'home/home.html')
    


def about(request):
    messages.success(request, 'This is about page.')
    messages.error(request, 'This is about page.')
    return render(request, 'home/about.html')

def referenceBooks(request):
    messages.success(request, 'This is Reference Books Page')
    return render(request, 'home/referenceBooks.html')

def videos(request):
    messages.success(request, 'This is Our videos Page')
    return render(request, 'home/videos.html')

def about(request):
    messages.success(request, 'This is about page.')
    messages.error(request, 'This is about page.')
    return render(request, 'home/about.html')
    

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<4:
            messages.error(request, "Please fill the from correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, desc=desc, timeStamp=datetime.today())
            contact.save()
            messages.success(request, 'Your Massage has been sent!.')
    return render(request, 'home/contact.html')
     

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent).union(allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. please refine your query.")
    params = { 'allPosts': allPosts, 'query':query } 
    return render(request, 'home/search.html', params)


def handelSingup(request):
    if request.method =='POST':

        #Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #check for errorneous input

        #Create User

        myuser = User.objects.create_user()


    else:
        return HttpResponse("404 - Not Found")


