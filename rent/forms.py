from django import forms
from .models import RentalListing


class RentalListingForm(forms.ModelForm):
    class Meta:
        model = RentalListing

        fields = ['title', 'category', 'location', 'description', 'hourly_rate']