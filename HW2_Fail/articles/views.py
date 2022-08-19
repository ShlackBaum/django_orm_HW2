from django.shortcuts import render

from articles.models import Article, Scope, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    article_objects = Article.objects.all()
    # scope_objects = Scope.objects.all()
    # articlescope_objects = ArticleScope.objects.all()
    context = {"object_list" : article_objects,
               # "scopes" : scope_objects,
               # "articlescopes": articlescope_objects
               }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
