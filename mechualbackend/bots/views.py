from django.http import HttpResponse
from django.shortcuts import render
from .models import Robot, Part, Controls, Button, Slider, ValueDisplay
# Create your views here.

def index(request):
    return render(request, 'index.html')
def lobby(request):
    return render(request, 'chat/lobby.html', )

def createbot(request):
    if request.method == 'GET':
        R = Robot.objects.create(name="Mechbot",
                             type="UGV",
                             year="2022",
                             serial_number="1")
        C = Controls.objects.create(name="Mechbot Controls")

        for i in range(1, 7):
            S = Slider.objects.create(name="CH" + str(i),
                                      description="CHANNEL " + str(i),
                                      value=1000,
                                      max_value=1000,
                                      min_value=2000)
            C.slider.add(S)
        C.save()
        R.controls.add(C)
        R.save()
        return HttpResponse("Bot created")
