from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm

def home(request):
    rooms = Room.objects.all()
    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'app1/home.html', context)

def room(request, pk):
    r = Room.objects.get(id=pk)
    topics = Topic.objects.all()
    context = {'room': r, 'topics': topics}
    return render(request, 'app1/room.html', context)

def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'app1/room_form.html', context)

def edit_room(request, pk):
    r = Room.objects.get(id=pk)
    form = RoomForm(instance=r)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=r)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'app1/room_form.html', context)

def delete_room(request, pk):
    r = Room.objects.get(id=pk)
    if request.method == 'POST':
        r.delete()
        return redirect('home')
    context = {'obj': r}
    return render(request, 'app1/delete.html', context)