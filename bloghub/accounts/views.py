from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from .form import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import logout




'''This is used to open user registeration if it has not been registered '''

'''def register_user(request):
    return render(request,"acct/user_register.html")'''

'''This is used to login in website after checking it is already registered or not '''



def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        try:
            # Check if the user exists
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # If the user does not exist, display an error message
            messages.error(request, "User does not exist.")
            return redirect('accounts:login_it')

        # Attempt to authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # If authentication is successful, log in the user
            login(request, user)
            # Redirect to the index page
            return redirect("myblogapp:index")
        else:
            # If authentication fails due to incorrect password, display error message
            messages.error(request, "Incorrect password.")

        # Redirect back to the login page
        return redirect('accounts:login_it')
    else:
        # If the request method is not POST, render the login form
        return render(request, "acct/login.html")

    
'''This is used to register the user so that they can login in '''

def add_user(request):
    if request.method =="POST":
        
        form=RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            username_t=form.cleaned_data['username']
            password_t=form.cleaned_data['password1']
            
            user=authenticate(request,username=username_t,password=password_t)
            login(request,user)
            messages.success(request,("Registration successfull"))
            return redirect('myblogapp:index')
    else:   
        form=RegisterForm()


    return render(request,'acct/user_register.html',context={'form':form})

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('myblogapp:home_hai')  # Redirect to the desired page after logout
    else:
        # If the request method is GET, simply redirect to the index page without logging out
        return redirect('myblogapp:index')
            

