from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Restaurant

# Create your views here.

# Create your views here.
def index(request):
    return render(request, "index.html")

def open_signin(request):
    # return HttpResponse("Sign In")
    return render(request, "signin.html")

def open_signup(request):
    return render(request, "signup.html")

def signup(request):
    #return HttpResponse("Recieved")
    if request.method == 'POST':
        # Fetching data from the form
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')

        try:
            Customer.objects.get(username=username)
            return HttpResponse("username alredy taken. please use other")
        
        except:
        #creating a customer table
            Customer.objects.create(username = username,
                                password = password,
                                email = email,
                                mobile = mobile,
                                address = address)
            return render(request, 'signin.html')

def signin(request):
    if request.method == 'POST':
        # Fetching data from the form
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Check if a user exists with the provided credentials
            customer = Customer.objects.get(username=username, password=password)
            if username == 'admin':
                return render(request, 'admin_home.html', {'customer': customer})
            else:
                return render(request, 'customer_home.html')
        except Customer.DoesNotExist:
            # If credentials are invalid, show a failure page
            return render(request, 'fail.html')
    else:
        return HttpResponse("Invalid request")
    
# adding new restaurants
def open_add_restaurant(request):
    return render(request, 'add_restaurant.html')

def open_show_restaurant(request):
    return render(request,'show_restaurant.html')

def add_restaurant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.POST.get('picture')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')

        try:
            Restaurant.objects.get(name = name)
            return HttpResponse("Restaurant already exsits")
        except:
            Restaurant.objects.create(name = name,
                                       picture = picture,
                                       cuisine = cuisine,
                                       rating = rating)
            
            #collecting all data to a variable
            restaurants = Restaurant.objects.all()
            #sending all objects data to frontend
            return render(request, 'show_restaurants.html', {"restaurants" : restaurants})