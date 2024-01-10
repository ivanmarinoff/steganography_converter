"""steg_app URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from steganography.users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('steganography.audio_steg.urls')),
    path('login/', user_views.LoginView.as_view(), name="login"),
    path('logout/', user_views.LogoutView.as_view(), name="logout"),
    path('signup/', user_views.RegisterView.as_view(), name="signup"),

    path('blog/', include('steganography.crypto_blog.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
