from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Test"),
    path('add-spent', views.add_spent, name="add-spent")
]
