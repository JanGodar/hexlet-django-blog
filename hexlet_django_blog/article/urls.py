from django.urls import path

from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleFormCreateView, ArticleFormEditView
#from hexlet_django_blog.article.views import ArticleCommentsView

urlpatterns= [
    path('', IndexView.as_view()),
    path('<int:id>/edit', ArticleFormEditView.as_view(), name='articles_update'),
    path('<int:id>/', ArticleView.as_view(), name='app-id'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create')

#    path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view())
]