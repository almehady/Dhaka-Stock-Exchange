from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("code/", views.scrape_company_code, name="code"),
]