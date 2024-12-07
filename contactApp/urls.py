from django.urls import path

# from homeApp.urls import urlpatterns
from . import views
app_name='contactApp'
urlpatterns=[
    path('contact/',views.contact,name='contact'),
    path('recruit/',views.recruit,name='recruit'),
]