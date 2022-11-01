
from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard),
    path('login', views.Login),
    path('signup', views.Signup),
]
