from django.views.generic import ListView, DetailView
from . import models
from django.http import Http404
from django.urls import reverse
from django_countries import countries
from django.shortcuts import render, redirect


class HomeView(ListView):
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class RoomDetail(DetailView):
    model = models.Room

# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/room_detail.html", {'room': room})
#     except  models.Room.DoesNotExist:
#         raise Http404()

def search(request):
    city = request.GET.get('city', "Anywhere")
    city = str.capitalize(city)
    room_types = models.Room.objects.all()
    return render(
        request,
        "rooms/search.html",
        {
            "city": city,
            "countries": countries,
            "room_types": room_types
        }
    )