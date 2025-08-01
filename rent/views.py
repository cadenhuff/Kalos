from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import RentalListing, Review
from .forms import RentalListingForm, ReservationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
# Create your views here.



def index(request):
    #if request.method == ""
    listings = RentalListing.objects.all()
    return render(request, "rent/landing_page.html",
                  {"listings":listings})


def listing_page(request, listing_id):
    listing = get_object_or_404(RentalListing, id = listing_id)
    reviews = Review.objects.filter(listing = listing)
    return render(request, "rent/listing_page.html",{"listing": listing, "reviews": reviews})


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


@login_required
def make_reservation(request, listing_id):
    listing = get_object_or_404(RentalListing, pk = listing_id)
    form = ReservationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            
            reservation = form.save(commit = False)
            reservation.reserver = request.user
            reservation.listing = listing
            try:
                reservation.save()
                messages.success(request,"Reservation successful!")
                return redirect('rent:index')
            except ValidationError as e:
                form.add_error(None, e.message)

    return render(request, 'rent/make_reservation.html', {'form':form, 'listing': listing})





