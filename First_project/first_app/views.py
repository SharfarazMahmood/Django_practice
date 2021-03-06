from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from first_app.models import Musician, Album
from first_app import forms
##import modules
from django.db.models import Avg
from django.http import HttpResponse

# Create your views here.

## class based views
class IndexView(ListView):
    context_object_name = 'musician_list'
    model = Musician
    template_name = 'first_app/index.html'

class AddMusician(CreateView):
    fields = ('first_name', 'last_name', 'instrument')
    model = Musician
    template_name = 'first_app/musician_form.html'

class MusicianDetail(DetailView):
    context_object_name = 'musician'
    model = Musician
    template_name = 'first_app/musician_detail.html'

class MusicianUpdate(UpdateView):
    fields = ('first_name', 'last_name', 'instrument')
    model = Musician
    template_name = 'first_app/musician_form.html'

class MusicianDelete(DeleteView):
    context_object_name = 'musician'
    model = Musician
    ## important
    success_url = reverse_lazy('first_app:index')
    template_name = 'first_app/delete_musician.html'



## Template view
# class IndexView(TemplateView):
#     template_name = 'first_app/index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['sample_text'] = 'sample_text 1'
#         context['sample_num'] = 56
#         return context


## second
def index_def(request):
    musician_list = Musician.objects.order_by("first_name")
    dict = {'title':"Home Page",
            'musician_list':musician_list}
    return render(request, 'first_app/index.html', context=dict)
    # return HttpResponse('Hello -__-')

def musician_form(request):
    form = forms.MusicianForm()
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index_def(request)
    dict = {'title':"Add Musician",
            'musician_form':form}
    return render(request, 'first_app/musician_form.html', context=dict)

def album_form(request):
    form = forms.AlbumForm()
    if request.method =='POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index_def(request)
    dict = {'title':"Add Album",
            "album_form":form}
    return render(request, 'first_app/album_form.html', context=dict)

def album_list(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    album_list = Album.objects.filter(artist_id=artist_id).order_by('name','release_date')
    artist_avg_rating = Album.objects.filter(artist_id=artist_id).aggregate( Avg('num_stars') )
    dict = {'title':"Album list",
            'artist_info':artist_info,
            'album_list':album_list,
            'artist_avg_rating':artist_avg_rating}
    return render(request, 'first_app/album_list.html', context=dict)


def edit_album(request, album_id):
    album_info = Album.objects.get(pk=album_id)
    form = forms.AlbumForm(instance=album_info)
    dict = {'title':"Edit Album",
            'edit_form':form,
            }
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album_info)
        if form.is_valid():
            form.save(commit=True)
            dict.update({'success_text':"Successfully Updated!"})
    dict.update({'edit_form':form})
    dict.update({'album_id':album_id})
    return render(request, 'first_app/edit_album.html', context=dict)

def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id).delete()
    dict = {'delete_success':"Album Successfully Deleted !"}
    return render(request, "first_app/delete.html", context=dict)

def delete_artist(request, artist_id):
    musician = Musician.objects.get(pk=artist_id).delete()
    dict = {'delete_success':"Musician Successfully Deleted !"}
    return render(request, "first_app/delete.html", context=dict)

def all_musicians(request):
    all_musicians = Musician.objects.order_by("first_name")
    dict = {'title':"Musicians",
            'musician_list':all_musicians}
    return render(request, 'first_app/all_musicians.html', context=dict)

def all_albums(request):
    all_albums = Album.objects.order_by("name")
    dict = {'title':"Albums",
            'album_list':all_albums}
    return render(request, 'first_app/all_albums.html', context=dict)
### first try
#
# def home (request):
#     return HttpResponse("<h1>home page from first app(o_o) </h1>  <a href='contact/'>Contact</a> <a href='about/'>About us</a>")
#
# def contact (request):
#     return HttpResponse("<h1>Contact page from first app(o_o) </h1> <a href='/first_app/'>Homepage</a> <a href='/first_app/about/'>About us</a>")
#
# def about (request):
#     return HttpResponse("<h1>About us from first app(o_o) </h1> <a href='/first_app/'>Homepage</a> <a href='/first_app/contact'>Contact</a>")
#
# def test (request):
#     return HttpResponse("<h2>first_app test case(o_o)</h2>")
#
# def index(request):
#     ## SELECT * FROM Musician ORDER BY first_name
#     musician_list = Musician.objects.order_by("first_name")
#     dict = {'sample_text':'This is a Sample text',
#             'sample_num':'5',
#             'album':Album.objects.get(pk=1),
#             }
#     return render(request, "first_app/index.html", context=dict) #
#
# def form(request):
#     new_form = forms.MusicianForm()
#
#     if request.method == 'POST':
#         new_form = forms.MusicianForm(request.POST)
#
#         if new_form.is_valid():
#             new_form.save(commit=True)
#             return index(request)
#     dict = {'test_form':new_form}
#     return render(request, "first_app/form.html", context=dict) #
# #
# # def form2 (request):
# #     new_form = forms.user_form()
# #     dict = {"test_form":new_form,
# #             "heading_1":"This form is created using django library"}
# #
# #     # to check if the form is submitted
# #     if request.method == 'POST':
# #         new_form = forms.user_form(request.POST)
# #         dict.update({"test_form":new_form})  ############# this line must be added to see ERRORS in the html view
# #
# #         if new_form.is_valid():
# #             user_name = new_form.cleaned_data['user_name']
# #             age = new_form.cleaned_data['age']
# #             user_dob = new_form.cleaned_data['user_dob']
# #             user_email = new_form.cleaned_data['user_email']
# #             boolean_field = new_form.cleaned_data['boolean_field']
# #             char_field - new_form.cleaned_data['char_field']
# #
# #             dict.update({'user_name': user_name })
# #             dict.update({'user_dob': user_dob})
# #             dict.update({'user_email': user_email})
# #             dict.update({'boolean_field': boolean_field})
# #             dict.update({'char_field': char_field})
# #             dict.update({'form_submited': "Yes"})
# #     return render(request, "first_app/form.html", context=dict)
# #
