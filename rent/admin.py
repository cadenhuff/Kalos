from django.contrib import admin
from .models import *
# Register your models here.


class ArtistAdmin(admin.ModelAdmin):
    list_display = ["name"]


class ArtworkPostingAdmin(admin.ModelAdmin):
    list_display = ["title", "creator"]

class RentalListingAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "location", "description", "hourly_rate"]

admin.site.register(Artist, ArtistAdmin)
admin.site.register(ArtworkPosting, ArtworkPostingAdmin)
admin.site.register(RentalListing, RentalListingAdmin)