from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.catalog_func),
    path('', views.main),
    path('bookwishes', views.wishes),
]