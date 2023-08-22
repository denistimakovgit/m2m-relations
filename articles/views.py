from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    context = {}

    object_list = Article.objects.all()
    object_list2 = Article.objects.prefetch_related('category')
    print(object_list)
    print(object_list2)
    context = {'object_list': object_list2}
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
