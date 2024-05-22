from django.shortcuts import render
from django.views import View
# from django.http import HttpResponse


class Article(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'articles.html', context= {
            'name': 'name_page',
            'tags': kwargs['tags'],
            'article_id': kwargs['article_id']
        })
