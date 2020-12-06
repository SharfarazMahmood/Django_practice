from django.shortcuts import render
from first_app.models import Musician, Album
from first_app import forms
##import modules
from django.db.models import Avg
from django.http import HttpResponse

# Create your views here.

## second try
def index(request):
    musician_list = Musician.objects.order_by("first_name")
    dict = {'title':"Home Page",
            'musician_list':musician_list}
    return render(request, 'first_app/index.html', context=dict)

def musician_form(request):
    form = forms.MusicianForm()
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    dict = {'title':"Add Musician",
            'musician_form':form}
    return render(request, 'first_app/musician_form.html', context=dict)

def album_form(request):
    form = forms.AlbumForm()
    if request.method =='POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    dict = {'title':"Add Album",
            "album_form":form}
    return render(request, 'first_app/album_form.html', context=dict)

def album_list(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    album_list = Album.objects.filter(artist=artist_id).order_by('name','release_date')
    artist_avg_rating = Album.objects.filter(artist=artist_id).aggregate( Avg('num_stars') )
    dict = {'title':"Album list",
            'artist_info':artist_info,
            'album_list':album_list,
            'artist_avg_rating':artist_avg_rating}
    return render(request, 'first_app/album_list.html', context=dict)

def edit_artist(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=artist_info)
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=artist_info)
        if form.is_valid():
            form.save(commit=True)
            return album_list(request, artist_id)
    dict = {'title':"Album list",
            'edit_form':form,
            }
    return render(request, 'first_app/edit_artist.html', context=dict)


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
