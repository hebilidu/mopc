
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    # path('', include('social_django.urls', namespace='social')),
    path('contacts/', include('contacts.urls')),
    path('photo/', include('photo.urls')),
    path('photologue/', include('photologue.urls', namespace='photologue')),
    path('blog/', include('blog.urls')),
    path('notes/', include('notes.urls')),
    path('genealogy/', include('genealogy.urls')),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)