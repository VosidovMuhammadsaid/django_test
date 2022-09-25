from django.urls import path
from . import views


urlpatterns = [
    path('<zodiak>/',views.get_info),
]
