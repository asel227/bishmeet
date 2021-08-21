
from django.contrib import admin

from django.urls import path, include


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('auth', include('djoser.urls')),
    path('auth', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include('apps.users.urls')),
    path('', include('apps.groups.urls')),
    path('', include('apps.events.urls')),
    path('', include('apps.profiles.urls')),

]
