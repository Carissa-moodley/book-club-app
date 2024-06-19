from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from . import views
from users import views as viewss
from django.conf.urls.static import static

# URLconf for main app 
# Map URLs for each view created
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('vote/', views.vote, name='vote'),
    path('signup/', viewss.signup, name='signup'),
    path('login/', viewss.login_view, name='login'),
    path('logout/', viewss.logout_view, name='logout'),
    path('', include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)