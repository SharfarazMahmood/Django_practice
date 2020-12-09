from django.contrib import admin

##import models
from first_app.models import Musician, Album


# Register your models here.
admin.site.register(Musician)
admin.site.register(Album)
