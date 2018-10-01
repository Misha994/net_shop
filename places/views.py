from places.models import Country, City
from django.views.generic import ListView, DetailView, CreateView, UpdateView


class CityList(ListView):
    model = City
    context_object_name = 'places'
    template_name = 'places/all_places.html'


class CityDetail(DetailView):
    model = City
    context_object_name = 'place'
    template_name = 'places/place_detail.html'


class CityCreate(CreateView):
    model = City
    fields = '__all__'
    template_name = 'places/place_form.html'


class CountryEdit(UpdateView):
    model = Country
    fields = '__all__'
    template_name = 'places/place_form.html'


class CountryCreate(CreateView):
    model = Country
    fields = '__all__'
    template_name = 'places/place_form.html'


class CityEdit(UpdateView):
    model = City
    context_object_name = 'place'
    fields = '__all__'
    template_name = 'places/place_form.html'
