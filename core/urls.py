
from django.contrib import admin

from django.urls import path, include


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls')),
    path('', include('apps.groups.urls')),
    path('', include('apps.events.urls')),
]
