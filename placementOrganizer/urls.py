from django.contrib import admin
from django.urls import path, include
from student import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    url(r'^advanced_filters/', include('advanced_filters.urls')),
] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

