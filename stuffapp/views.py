# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect
from stuffapp.models import Thing
from stuffapp.forms import StuffForm


def list_stuff(request):
    stuff = Thing.objects.all()
    return render(request, 'stuffapp/list_stuff.html', {'stuff': stuff})

def thing_detail(request, thing_id):
    thing = get_object_or_404(Thing, pk=thing_id)
    return render(request, 'stuffapp/thing_detail.html', {'thing': thing})

def create_stuff(request):
    if request.method == 'POST':
        form = StuffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-stuff')
    else:
        form = StuffForm()
    return render(request, 'stuffapp/create_stuff.html', {'form': form})

def edit_stuff(request, thing_id):
    thing = get_object_or_404(Thing, pk=thing_id)
    if request.method == 'POST':
        form = StuffForm(request.POST, instance=thing)
        if form.is_valid():
            form.save()
            return redirect('thing-detail', thing_id)
    else:
        form = StuffForm(instance=thing)
    return render(request, 'stuffapp/edit_stuff.html', {'form': form})
       
def delete_stuff(request, thing_id):
    thing = get_object_or_404(Thing, pk=thing_id)
    if request.method == 'POST':
        thing.delete()
        return redirect('/stuff/')
    return render(request, 'stuffapp/delete_stuff.html', {'thing': thing})