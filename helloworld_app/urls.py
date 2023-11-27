from django.urls import path
from . import views

urlpatterns = [
    path('html/', views.template_view, name="html"),
    path('json/', views.json_view, name="json")
]
