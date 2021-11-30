from django import forms
from .models import Film, Director, Category, RatingFilm


class AddFilmForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Film
        exclude = ['available_in_countries']
        labels = {
            'created_in_country': 'Country',
        }
        field_order = ['title','release_date', 'category', 'country']


class AddDirectorForm(forms.ModelForm):
    film = forms.ModelMultipleChoiceField(
        queryset=Film.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Director
        fields = '__all__'


class EditDirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        exclude = ['film']


class RatingFilmForm(forms.ModelForm):
    class Meta:
        model = RatingFilm
        fields = ['rating']