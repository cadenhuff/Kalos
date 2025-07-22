from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class ArtworkPosting(models.Model):
    title = models.CharField(max_length = 255)

    creator = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="artwork_postings")

    def __str__(self):
        return self.title
    



class RentalListing(models.Model):
    def __str__(self):
        return self.title
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    title = models.CharField(max_length = 255)
    

    LISTING_CHOICES = (
        ("photography", "Photography"),
        ("pottery", "Pottery"),
        ("other", "Other")

    )

    category = models.CharField(
        max_length = 50,
        choices = LISTING_CHOICES,
        default = "pottery",
        blank = False
    )

    location = models.CharField(
        max_length=255,
        blank=True,
        default='',
        help_text='Enter a geographical address (e.g., 123 Main St, City, Country)'
    )




    description = models.TextField(
        blank=True,  # Allows the field to be empty in forms
        null=True,   # Allows NULL in the database
        default='',  # Sets a default empty string
        help_text='Enter a detailed description here.'
    )

    hourly_rate = models.DecimalField(
        max_digits = 10,
        decimal_places = 2,
        default = 0.0,
        help_text = "Hourly Rate in USD",
        blank = False
    )