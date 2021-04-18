from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, "MainFlight/index.html", {
        "flights": Flight.objects.all()
    })

def indflight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "MainFlight/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "nonpassengers": Passenger.objects.exclude(flights=flight).all()
    })
    
def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)

        return HttpResponseRedirect(reverse("indflight", args=(flight.id,)))