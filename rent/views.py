from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RentalListing
from .forms import RentalListingForm
from django.contrib.auth.decorators import login_required
# Create your views here.



def index(request):
    
    return render(request, "rent/landing_page.html")




def all_listings(request):
    listings = RentalListing.objects.all()
    return render(request, "rent/all_listings.html",
                  {"listings":listings})

@login_required
def create_listing(request):
    if request.method == "POST":
        create_form = RentalListingForm(request.POST)

        if create_form.is_valid():
            rental_listing = create_form.save(commit = False)
            rental_listing.owner = request.user
            rental_listing.save()
            return redirect('rent:index')

    else:
        create_form = RentalListingForm()
    return render(request, 'rent/create_listing.html', {"create_form": create_form})

def search_results(request):
    return


