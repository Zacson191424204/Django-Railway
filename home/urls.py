from django.urls import path
from home import views
urlpatterns = [
    path('', views.render_home, name='home')
]