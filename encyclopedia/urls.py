from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from . import util

#app_name = 'encyclopedia'


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/search", views.search, name="search"),
    path("wiki/random", views.random, name="random"),
    path("wiki/<entry>", views.entries, name="entry"),
    path("edit/<link>", views.edit, name="edit"),
    path("newpage", views.newpage, name="newpage"),

]
"""
for l in util.list_entries():
    urlpatterns += [
    path(f"wiki/{l}", views.entries, name=f"{l}"),
    ]

"""

