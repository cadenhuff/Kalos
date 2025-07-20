from django.shortcuts import render
from django.http import HttpResponse
from .models import RentalListing
# Create your views here.



def index(request):
    return render(request, "rent/landing_page.html")




def all_listings(request):
    listings = RentalListing.objects.all()
    return render(request, "rent/all_listings.html",
                  {"listings":listings})



def search_results(request):
    return

