"""profile_instagram URL Configuration"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

admin.site.site_header = 'Failure Resporting Systems'
admin.site.site_title = 'Administration'
admin.site.index_title = 'Failure Resporting Systems Administration'

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include(('profile_instagram.users.urls', 'users'), namespace='users')),
    path('', include(('profile_instagram.publications.urls', 'users'), namespace='publications')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
