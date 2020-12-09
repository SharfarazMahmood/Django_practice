from django.contrib import admin
from django.urls import path

##import APPs
from first_app import views
##import urls from all apps
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    ###path for apps urls file
    path('first_app/', include('first_app.urls') ),
    path('', include('first_app.urls') ),

]
