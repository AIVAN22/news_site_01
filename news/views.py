from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
import requests

# Create your views here.


def random(request):
    last_business_news = Business_news.objects.last()
    last_health_news = Health_news.objects.last()
    last_tech_news = Tech_news.objects.last()
    last_sport_news = Sport_news.objects.last()
    last_science_news = Science_news.objects.last()
    
    return render(
        request,
        "news/random.html",
        {
            "last_business_news": last_business_news,
            "last_health_news": last_health_news,
            "last_tech_news": last_tech_news,
            "last_sport_news": last_sport_news,
            "last_science_news": last_science_news,
        },
    )
    

def about(request):
    return render(request, "news/about.html")


def article(request, news_id):
    news_article = get_object_or_404(Business_news, id=news_id)
    return render(request, "news/article.html", {"news_article": news_article})


def article_health(request, news_id):
    news_article_health = get_object_or_404(Health_news, id=news_id)
    return render(
        request,
        "news/article_health.html",
        {"news_article_health": news_article_health},
    )


def article_tech(request, news_id):
    news_article_tech = get_object_or_404(Tech_news, id=news_id)
    return render(
        request,
        "news/article_tech.html",
        {"news_article_tech": news_article_tech},
    )


def article_sport(request, news_id):
    news_article_sport = get_object_or_404(Sport_news, id=news_id)
    return render(
        request,
        "news/article_sport.html",
        {"news_article_sport": news_article_sport},
    )


def article_science(request, news_id):
    news_article_science = get_object_or_404(Science_news, id=news_id)
    return render(
        request,
        "news/article_science.html",
        {"news_article_science": news_article_science},
    )


def business(request):
    business_info = Business_news.objects.all()
    paginator = Paginator(business_info, 5)
    page = request.GET.get("page")
    business_info = paginator.get_page(page)
    return render(
        request,
        "news/business.html",
        {"business_info": business_info},
    )


def health(request):
    health_info = Health_news.objects.all()
    paginator = Paginator(health_info, 5)
    page = request.GET.get("page")
    health_info = paginator.get_page(page)
    return render(
        request,
        "news/health.html",
        {"health_info": health_info},
    )


def tech(request):
    tech_info = Tech_news.objects.all()
    paginator = Paginator(tech_info, 5)
    page = request.GET.get("page")
    tech_info = paginator.get_page(page)
    return render(
        request,
        "news/tech.html",
        {"tech_info": tech_info},
    )


def sport(request):
    sport_info = Sport_news.objects.all()
    paginator = Paginator(sport_info, 5)
    page = request.GET.get("page")
    sport_info = paginator.get_page(page)
    return render(
        request,
        "news/sport.html",
        {"sport_info": sport_info},
    )


def science(request):
    science_info = Science_news.objects.all()
    paginator = Paginator(science_info, 5)
    page = request.GET.get("page")
    science_info = paginator.get_page(page)
    return render(
        request,
        "news/science.html",
        {"science_info": science_info},
    )

   

