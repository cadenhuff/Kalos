from django.urls import path
from . import views

app_name = 'rent'




urlpatterns = [
    path("", views.index, name = "index"),
    path("all_listings/", views.all_listings, name = "all_listings"),
    path("create_listing/", views.create_listing, name = "create_listing")
]



