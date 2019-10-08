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

def editDog(request, dogID):
    instanceOfTheModel = DogModel.objects.get(pk=dogID)
    if request.method == "POST":
        # save stuff
        newUserEdittedForm = DogForm(request.POST, instance=instanceOfTheModel)
        newUserEdittedForm.save()
        return HttpResponseRedirect("/dog/")

    form = DogForm(instance=instanceOfTheModel)
    context = {
        "form": form
    }
    return render(request, "DogApp/editDogForm.html", context)

def deleteDog(request, dogID):
    instanceOfTheModel = DogModel.objects.get(pk=dogID)
    instanceOfTheModel.delete()
    return HttpResponseRedirect("/dog/")