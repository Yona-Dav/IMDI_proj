from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import AddFilmForm, AddDirectorForm,EditDirectorForm
from .models import Film, Director, CommentFilm, RatingFilm
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

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

class DirectorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'director/editDirector.html'
    model = Director
    form_class = EditDirectorForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class FilmDeleteView(DeleteView):
    model = Film
    template_name = 'delete_view.html'
    success_url = reverse_lazy('homepage')
    success_message = "The film was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message  % obj.__dict__)
        return super(FilmDeleteView, self).delete(request, *args, **kwargs)


class FilmUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'film/editFilm.html'
    model = Film
    form_class = AddFilmForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = CommentFilm
    fields = ['content']
    template_name = 'film/film_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['film'] = Film.objects.get(id=self.kwargs['film_id'])
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        film_id = self.kwargs['film_id']
        film = Film.objects.get(id=film_id)
        self.object.film = film
        self.object.save()
        return super().form_valid(form)


class RatingCreateView(LoginRequiredMixin, CreateView):
    model = RatingFilm
    fields = ['ratings']
    template_name = 'film/film_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['film'] = Film.objects.get(id=self.kwargs['film_id'])
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        film_id = self.kwargs['film_id']
        film = Film.objects.get(id=film_id)
        self.object.film = film
        self.object.save()
        return super().form_valid(form)

