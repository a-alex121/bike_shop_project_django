from django.urls import path
from . import views
urlpatterns = [
	path("", views.index, name="index"),
    path("pag1", views.pag1, name="f"),
    path("pag2", views.pag2, name="g"),

]
