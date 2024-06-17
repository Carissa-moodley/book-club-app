from django.urls import path
from . import views


app_name = 'users'
# URLconf for users app 
# Map URLs for each view created
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
  
]