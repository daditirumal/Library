from django.urls import path
from . import views
urlpatterns = [
    path('person/', views.person, name='person'),

    
]