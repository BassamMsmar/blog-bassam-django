from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from .views import signup, profile, profile_update


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile_update/', profile_update, name='profile_update'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)