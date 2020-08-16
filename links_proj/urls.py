from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from accounts.views import public_profile, login, register, logout, profile_edit
from links.views import link_list, link_create, link_clicked, appearance, stats, settings as link_settings, link_edit
from .views import index

urlpatterns = [
    path('', index, name="index"),
    # path('links/', include('links.urls')),
    path('links/', link_list, name='link_list'),
    path('links/create/', link_create, name='link_create'),
    path('links/edit/<int:link_id>', link_edit, name='link_edit'),
    path('links/link_clicked/', link_clicked, name='link_clicked'),
    # path('links/appearance/', appearance, name='appearance'),
    # path('links/stats/', stats, name='stats'),
    # path('links/settings/', link_settings, name='settings'),

    path('api/stats', include('stats.urls')),

    # path('accounts/', include('accounts.urls')),
    path('auth/login/', login, name='login'),
    path('auth/register/', register, name='register'),
    path('auth/logout/', logout, name='logout'),
    path('profile/edit/', profile_edit, name="profile_edit"),
    path('profile/<str:uname>/', public_profile, name="public_profile"),


    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
     name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
        name="password_reset_complete"),


    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/change-password.html'), name="password_change"),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),



    path('panel/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
