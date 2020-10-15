from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows),
    path('shows/new', views.new_show),
    path('create_new_show', views.create_new_show),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<int:id>/destroy', views.destroy),
    path('update', views.update),
    path('shows/<int:id>', views.show)
]