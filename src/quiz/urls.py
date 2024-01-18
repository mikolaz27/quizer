from django.urls import path

from quiz.views import bitcoin

urlpatterns = [
    path("bitcoin/", bitcoin, name="bitcoin"),
]
