from django.contrib import admin
from django.urls import path, include
from django.conf import settings

# URLs for things like admin config, 3rd party apps, etc.
main_urls = [
    path('api/', include([
        # Admin
        path(settings.ADMIN_URL, admin.site.urls),

        # Authentication
        path('auth/', include([
            path('', include('djoser.urls')),
            path('', include('djoser.urls.jwt')),
        ]))
    ])),
]

# URLs for project's apps
apps_urls = [
    path('api/v1/', include([
        # Insert your apps' urls here like this:
        # path('{relative_path}', include('{{cookiecutter.project_slug}}.{app_name}.urls')),
    ])),
]

urlpatterns = main_urls + apps_urls