from django.shortcuts import render, redirect

from event.forms import EventForm
from event.models import Event, Bend, BendEvent


# Create your views here.
def index(request):
    events = Event.objects.filter(user=request.user).all()
    return render(request, "index.html", {"events": events})


def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST, files=request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.poster = form.cleaned_data['poster']
            event.name = form.cleaned_data['name']
            event.date = form.cleaned_data['date']
            event.time = form.cleaned_data['time']
            event.save()
            bends = form.cleaned_data['bends'].split(",")
            new_event = Event.objects.filter(pk=event.pk).first()
            for bend in bends:
                new_bend = Bend.objects.filter(name=bend).first()
                if new_bend:
                    new_bend.num = new_bend.num + 1
                    new_bend.save()
                    BendEvent.objects.create(bend=new_bend, event=event)
                    return redirect('index')
    else:
        form = EventForm()

        return render(request, "add_event.html", {"form": form})
