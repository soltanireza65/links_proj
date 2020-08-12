from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts.views import public_profile, login, register, logout
from links.views import link_list, link_create, link_clicked, appearance, stats, settings as link_settings
from .views import index

urlpatterns = [
    path('', index, name="index"),


    # path('links/', include('links.urls')),
    path('links/', link_list, name='link_list'),
    path('links/create/', link_create, name='link_create'),
    path('links/link_clicked/', link_clicked, name='link_clicked'),
    path('links/appearance/', appearance, name='appearance'),
    path('links/stats/', stats, name='stats'),
    path('links/settings/', link_settings, name='settings'),

    path('api/stats', include('stats.urls')),

    # path('accounts/', include('accounts.urls')),
    path('auth/login/', login, name='login'),
    path('auth/register/', register, name='register'),
    path('auth/logout/', logout, name='logout'),
    path('profile/<str:uname>/', public_profile, name="public_profile"),

    path('panel/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
