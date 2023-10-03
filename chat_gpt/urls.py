from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.chat.urls', 'apps.chat'))),
    path('', include(('apps.user.urls', 'apps.user'))),

    path('docs/schema', SpectacularAPIView.as_view(), name='schema'),
    path('docs/swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger')
]
