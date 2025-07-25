from django import forms
from .models import RentalListing, Reservation


class RentalListingForm(forms.ModelForm):
    class Meta:
        model = RentalListing

        fields = ['title', 'category', 'location', 'description', 'hourly_rate']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs = {'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type':'date'}),
        }

