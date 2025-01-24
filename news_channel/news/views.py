from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import News

def news_list(request):
    news = News.objects.all()
    return render(request, 'news/news_list.html', {'news': news})

def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    return render(request, 'news/news_detail.html', {'news_item': news_item})

