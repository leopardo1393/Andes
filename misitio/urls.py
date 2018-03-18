from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    
    url(r'^safety/', include('safety.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('safety.urls')),
]
