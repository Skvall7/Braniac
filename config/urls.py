import debug_toolbar
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path('', RedirectView.as_view(url='mainapp/')),
    path("social_auth/", include("social_django.urls", namespace="social")),
    path('mainapp/', include('mainapp.urls', namespace='mainapp')),
    path("authapp/", include("authapp.urls", namespace="authapp")),
]

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

