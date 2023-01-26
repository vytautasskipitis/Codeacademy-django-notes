from django.urls import path

from . import views

# Reikia Auth middleware arba router blocking
urlpatterns = [
  path("<int:id>", views.index, name="index"),
  path("", views.home, name="home"),
  path("home_login/", views.home_login, name="home_login"),
  path("create/", views.create, name="create"),
  path("view/", views.view, name="view"),
  path("delete/<int:id>", views.delete, name="delete"),
]

