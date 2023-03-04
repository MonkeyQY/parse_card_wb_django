from django.urls import path
from .views import parse_cards

urlpatterns = [
    path("parse_card/", parse_cards, name="parse_card"),
]
