from django.urls import path

from . import views
from django.conf.urls.static import static
app_name = "game"
urlpatterns = [
    path("", views.index, name="index"),
    #path("page/", views.page, name="index"),
]