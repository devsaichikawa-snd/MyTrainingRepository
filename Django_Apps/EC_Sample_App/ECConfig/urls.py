from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
#from allauth.socialaccount.providers.google.urls import urlpatterns as google_url

from . import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('oauth_accounts/', include('google_url')), # googleのみ
    path('oauth_accounts/', include('allauth.urls')), # AllAuth
    path('accounts/', include('accounts.urls')),
    path('stores/', include('stores.urls')),
]


if settings.DEBUG:
    urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
