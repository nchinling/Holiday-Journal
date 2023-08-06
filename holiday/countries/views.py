from django.shortcuts import render,get_object_or_404, redirect
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Destination, City, MapImage, Photo
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
# from django.db import IntegrityError
from .forms import NewUserForm
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import base64



class CityField(forms.CharField):
    def prepare_value(self, value):
        if isinstance(value, list):
            return ", ".join(city.name for city in value)
        return value
    def clean(self, value):
            if not value:
                return []
            if isinstance(value, str):
                city_names = value.split(",") 
                cities = []
                for city_name in city_names:
                    city, _ = City.objects.get_or_create(name=city_name.strip())
                    cities.append(city)
                return cities
            return value

class NewDestinationForm(forms.ModelForm):
    country = forms.CharField(max_length=64)
    # city = forms.CharField(max_length=64)
    city = CityField(max_length=100)
    entry = forms.CharField(widget=forms.Textarea)
    fromDate = forms.DateField(label='From', widget=forms.DateInput(attrs={'type': 'date'}))
    toDate = forms.DateField(label='To', widget=forms.DateInput(attrs={'type': 'date'}))
    map_image = forms.ImageField(required=False)


    class Meta:
        model = Destination
        fields = ['country','city','entry', 'fromDate', 'toDate', 'map_image']
    

    def save(self, commit=True):
        destination = super().save(commit=False)
        cities_data = self.cleaned_data.get('city')
        map_image_data = self.cleaned_data.get('map_image')
   

        if commit:
            destination.save()
            
        if cities_data:
            destination.city.clear()  # Remove existing city relationships
            for city in cities_data:
                destination.city.add(city)
        
        # save photos
        photos_data = self.cleaned_data.get('photos')
        if photos_data:
            for photo in photos_data:
                Photo.objects.create(destination=destination, image=photo)
        
        if map_image_data:
            map_image = MapImage.objects.create(destination=destination, image_data=map_image_data)

        return destination

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("countries:index")
            # return HttpResponseRedirect(reverse("countries:index"))
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="countries/register.html", context={"register_form":form})


def index(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse("countries:login"))

    return render(request, "countries/index.html", {
        "destinations": Destination.objects.all().order_by('-id'),
     
    })



def personal(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("countries:login"))

    user = request.user.username
    destinations = Destination.objects.filter(username=user).order_by('-id')
    return render(request, "countries/index.html", {
        "destinations": destinations,
    })

def search(request):
    query = request.GET.get('query')
    destinations = Destination.objects.filter(Q(country__icontains=query) | Q(city__name__icontains=query)).order_by('-id')
    return render(request, "countries/index.html", {
        "destinations": destinations,
    })

def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("countries:index"))
        # Otherwise, return login page again with new context
        else:
            return render(request, "countries/login.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "countries/login.html")

def logout_view(request):
    logout(request)
    return render(request, "countries/login.html", {
                "message": "Logged Out"
            })
# Add a new country:
# def add(request):
#     return render(request, "countries/add.html")

# Add a new country:
def add(request):

    print("View function 'add' is called.") 
    
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("countries:login"))

    destination = None
    if request.method == "POST":
        form = NewDestinationForm(request.POST, request.FILES)
        if form.is_valid():
            destination = form.save() 

            # destination.username = request.user.username
            destination.username = request.user.username
            destination.save() 

            # Save the map image data to the database
            map_image_data = request.POST.get('map_image')
            MapImage.objects.create(destination=destination, image_data=map_image_data)

            photos_data = request.FILES.getlist('photos')
            for photo in photos_data:
                Photo.objects.create(destination=destination, image=photo) 
            
    
            # photos_data = request.FILES.getlist('photos')
            # for photo in photos_data:
            #     Photo.objects.create(destination=destination, image=photo) 
          
          
            return HttpResponseRedirect(reverse("countries:index"))
    else:
        form = NewDestinationForm()
    
    return render(request, "countries/add.html", {"form": form})


def destination(request, destination_id):
    destination = Destination.objects.get(id=destination_id)
    return render(request, "countries/destination.html", {
        "destination": destination
    })


def edit(request, destination_id):
    destination = get_object_or_404(Destination, pk=destination_id)

    if not request.user.username == destination.username:
        return HttpResponseRedirect(reverse("countries:index"))

    if request.method == 'POST':
        form = NewDestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            photos_data = request.FILES.getlist('photos')
            for photo in photos_data:
                Photo.objects.create(destination=destination, image=photo) 

            return HttpResponseRedirect(reverse("countries:index"))
    else:
        form = NewDestinationForm(instance=destination)

    city_name = ", ".join(city.name for city in destination.city.all())
    return render(request, "countries/edit.html", {'form': form, 'city_name': city_name, 'destination': destination})


def delete_photo(request):
    if request.method == "POST" and request.user.is_authenticated:
        photo_id = request.POST.get("photo_id")
        try:
            photo = Photo.objects.get(id=photo_id)
            photo.delete()
            return JsonResponse({"message": "Photo deleted successfully."})
        except Photo.DoesNotExist:
            return JsonResponse({"error": "Photo not found."}, status=404)
    return JsonResponse({"error": "Invalid request."}, status=400)


def delete_journal(request, destination_id):
    if request.method == "POST" and request.user.is_authenticated:
        # destination = get_object_or_404(Destination, pk=destination_id)
        destination = Destination.objects.get(pk=destination_id)
        
       
        if request.user.username == destination.username:
            destination.delete()
            return redirect("countries:index")
    # If the user is not authenticated or not allowed to delete, you can handle it accordingly
    return HttpResponseForbidden("You are not allowed to delete this entry.")

