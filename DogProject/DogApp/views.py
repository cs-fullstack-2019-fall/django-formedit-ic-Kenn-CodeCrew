from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import DogModel
from .forms import DogForm

# Create your views here.
def blankURL(request):
    return HttpResponse("Bad URL")

def index(request):
    if request.method == 'POST':
        userSubmittedForm = DogForm(request.POST)
        if userSubmittedForm.is_valid():
            userSubmittedForm.save()
    context = {
        "allDogsArray": DogModel.objects.all(),
        "blankForm": DogForm()
    }
    return render(request, 'DogApp/index.html', context)

def editDog(request):
    context = {

    }
    return render(request, "DogApp/editDogForm.html", context)

def deleteDog(request):
    context = {

    }
    return render(request, "DogApp/deleteDogForm.html", context)