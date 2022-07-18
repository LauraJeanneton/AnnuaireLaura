
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', RedirectView.as_view(url='/repertoire/')),
    path('repertoire/',include('repertoire.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
