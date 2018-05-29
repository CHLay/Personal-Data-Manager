from django.urls import path

from . import views

app_name = 'budget'
urlpatterns = [
    path('submit/', views.submit, name='submit'),
]