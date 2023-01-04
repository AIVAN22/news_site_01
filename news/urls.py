from django.urls import path
from . import views


urlpatterns = [
    path("", views.random, name="random"),
    path("about", views.about),
    path("business", views.business, name="business"),
    path("health", views.health, name="health"),
    path("tech", views.tech, name="tech"),
    path("sport", views.sport, name="sport"),
    path("science", views.science, name="science"),
    path("article/<int:news_id>/", views.article, name="article"),
    path("article_health/<int:news_id>/", views.article_health, name="article_health"),
    path("article_tech/<int:news_id>/", views.article_tech, name="article_tech"),
    path("article_sport/<int:news_id>/", views.article_sport, name="article_sport"),
    path(
        "article_science/<int:news_id>/", views.article_science, name="article_science"
    ),
]
