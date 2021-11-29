from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import AddFilmForm, AddDirectorForm,EditDirectorForm
from .models import Film, Director
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

# Create your views here.

class FilmListView(ListView):
    template_name = 'homepage.html'
    model = Film
    #queryset = Film.object.all().order_by('-release_date')
    context_object_name = 'films'



class FilmCreateView(CreateView):
    template_name = 'film/addFilm.html'
    model = Film
    form_class = AddFilmForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())


class FilmUpdateView(UpdateView):
    template_name = 'film/editFilm.html'
    model = Film
    form_class = AddFilmForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())


class DirectorCreateView(CreateView):
    template_name = 'director/addDirector.html'
    model = Director
    form_class = AddDirectorForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        film = form.cleaned_data['film']
        print(film.first())
        print(self.object)
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

class DirectorUpdateView(UpdateView):
    template_name = 'director/editDirector.html'
    model = Director
    form_class = EditDirectorForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())