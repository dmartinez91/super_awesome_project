from django.urls.resolvers import URLPattern
from . import views
from django.urls import path, include
from django.contrib import admin

urlpattern = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls'))
]