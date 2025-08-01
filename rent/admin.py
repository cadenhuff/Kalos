from django.contrib import admin
from .models import *
# Register your models here.



class RentalListingAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "location", "description", "hourly_rate"]

class ReservationAdmin(admin.ModelAdmin):
    list_display = ["listing", "reserver", "start_date", "end_date"]

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["reviewer", "listing", "review", "created_date"]
admin.site.register(RentalListing, RentalListingAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Review, ReviewAdmin)