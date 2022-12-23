from django.shortcuts import redirect, render

from people.models import People

# Create your views here.
def home(request):
    people = People.objects.all()
    return render(request, "people.html", {"people": people})


def save(request):
    vname = request.POST.get("name")
    vemail = request.POST.get("email")
    People.objects.create(name=vname, email=vemail)
    people = People.objects.all()
    return render(request, "people.html.", {"people": people})


def edit(request, id):
    person = People.objects.get(id=id)
    return render(request, "update.html", {"person": person})


def update(request, id):
    vname = request.POST.get("name")
    person = People.objects.get(id=id)
    person.name = vname
    person.save()
    return redirect(home)


def delete(request, id):
    person = People.objects.get(id=id)
    person.delete()
    people = People.objects.all()
    return render(request, "people.html", {"people": people})
