from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Max



# Create your views here.

def top_rated(request):
    highest_ratings = myrating.objects.values('blog').annotate(highest_rating=Max('rating'))

    
    blogs_with_highest_ratings = []
    for rating_info in highest_ratings:
        blog = myblog.objects.get(pk=rating_info['blog'])
        highest_rating = rating_info['highest_rating']
        
        blogs_with_highest_ratings.append({'blog': blog, 'highest_rating': highest_rating})

    
    return render(request, 'top_rated_blogs.html', {'blog_list': blogs_with_highest_ratings})


def add_blog(request):
    if request.method == 'POST':
        # try:
            data = request.POST
            new_blog = myblog.objects.create(
                blog_name=data.get('blog_name'),
                description=data.get('description'),
                content=data.get('content'),
                image=request.FILES.get('image'),
                
            )
            
            return redirect("myblogapp:index")
    else :
            return render(request, "index.html")
        
    
def update(request , myblog_id):
       blog = get_object_or_404(myblog, pk=myblog_id)

       if request.method == 'POST':
            
        # Update the specified fields with the new values
            blog_name_get=request.POST.get('blog_name')
            blog_description=request.POST.get('description')
            blog_content=request.POST.get('content')

            if blog_name_get:
                blog.blog_name =  blog_name_get
            if blog_description:
                blog.description = blog_description
            if blog_content:
                blog.content = blog_content
            
           
        
        # Save the updated blog object
            blog.save()
        
        # Redirect to a specific URL
            return HttpResponseRedirect(reverse('myblogapp:detail', args=[myblog_id]))
       
def delete(request , myblog_id ):
    blog=get_object_or_404(myblog,pk=myblog_id)       
    blog.delete()
    return HttpResponseRedirect(reverse('myblogapp:index'))

         
def give_rating(request, myblog_id):

    blog = get_object_or_404(myblog, pk=myblog_id)
    
    if request.method == 'POST':
        # Retrieve form data from POST request
        username = request.POST.get('username')
        email = request.POST.get('email')
        
        try:
            # Check if the user exists
            user = User.objects.get(username=username)
            rating_value = int(request.POST.get('rating'))

        except User.DoesNotExist :
            

            messages.error(request, "User does not exist.")
           
        
        
        except ValueError:
            messages.error(request, "Please Enter rating")
            return HttpResponseRedirect(reverse('myblogapp:detail', args=[myblog_id]))

          

        userone=User.objects.filter(username=username).first()
        
        user_rating = myrating.objects.filter(blog=blog, user=userone).first()
        if user_rating:
            
            user_rating.rating = rating_value
            user_rating.save()
        else:
            
            myrating.objects.create(blog=blog, user=userone, rating=rating_value)
            
        return HttpResponseRedirect(reverse('myblogapp:detail', args=[myblog_id]))
    

    
    
     
def home(request):
    return render(request,"home.html")


    

def index(request):
    blog_list=myblog.objects.all()
    rating_list=myrating.objects.all()
    context={"blog_list":blog_list}
    return render(request,"index.html", context )


def detail(request , myblog_id ):
    request_user = request.user
    blog_list= myblog.objects.get(pk=myblog_id)
    rating_list=myrating.objects.filter(blog=blog_list).order_by("-rating")
       
    myratingInst = myrating.objects.filter(blog=blog_list, user=request_user).last() if blog_list and request_user else None

    ratings = myratingInst.rating if myratingInst else "Please give rating"

    return render(request,"detail.html",{"blog_list":blog_list, "ratings": ratings,"rating_list":rating_list})

