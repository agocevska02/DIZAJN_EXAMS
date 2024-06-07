import random

from django.shortcuts import render, redirect

from app.forms import ReservationForm
from app.models import Reservation, Employee, Room


# Create your views here.
def index(request):
    rooms = Room.objects.filter(num_beds__lt=5).all()
    return render(request, "index.html", {"rooms": rooms})


def contact_us(request):
    form = ReservationForm()
    if request.method == 'POST':
        reservationForm = ReservationForm(request.POST, files=request.FILES)
        if reservationForm.is_valid():
            reservation = reservationForm.save(commit=False)
            reservation.user = request.user
            reservation.id_photo = reservationForm.cleaned_data['id_photo']
            reservation.start_date = reservationForm.cleaned_data['start_date']
            reservation.end_date = reservationForm.cleaned_data['end_date']
            reservation.code = random.randint(1, 999999)
            name_surname = reservationForm.cleaned_data['name_surname'].split(" ")
            print(name_surname[0])
            print(name_surname[1])
            employee = Employee.objects.filter(name=name_surname[0], surname=name_surname[1]).first()
            if employee:
                reservation.employer = employee
                reservation.save()
            return redirect("index")

    return render(request, "contact_us.html", {"form": form})
