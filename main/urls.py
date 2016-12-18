from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^articles/$', views.article, name="articles"),
    url(r'^imports/$', views.import_view, name="imports"),
    url(r'^articles/delete_article$', views.delete_article, name="delete_articles"),
    url(r'^imports/delete_import$', views.delete_imports, name="delete_imports"),
    url(r'^exports/$', views.export_view, name="exports"),
]
