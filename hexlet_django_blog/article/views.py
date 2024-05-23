from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from hexlet_django_blog.article.models import Article
from .forms import CommentArticleForm, ArticleForm
# from django.http import HttpResponse

class CommentArticleView(View):
    def get(self, request, *args, **kwargs):
        form = CommentArticleForm()
        return render(request, 'comment.html', {'form': form})

class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id= kwargs.get('id')
        article= Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})

    def post(self, request, *args, **kwargs):
        article_id= kwargs.get('id')
        article= Article.objects.get(id=article_id)
        form= ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('/articles/')

        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form= ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form= ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/articles/')
        return render(request, 'articles/create.html', {'form': form})

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article=get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })

# class ArticleCommentsView(View):
#     def get(self, request, *args, **kwargs):
#         comment=get_object_or_404(Comment, id=kwargs['id'], article__id=kwargs['article_id'])
#         return render(request, 'articles/comment.html')

class IndexView(View):
    
    def get(self, request, *args, **kwargs):
        articles= Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


# class Article(View):

#     def get(self, request, *args, **kwargs):
#         return render(request, 'articles.html', context= {
#             'name': 'name_page',
#             'tags': kwargs['tags'],
#             'article_id': kwargs['article_id']
#         })
