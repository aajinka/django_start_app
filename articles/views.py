
from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article, Category, Comment
from .forms import CreateArticle, EditArticle, CommentArticle 
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

def LikeView(request, pk):
    article = get_object_or_404(Article, id=request.POST.get('article_id'))
    liked = False
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
        liked = False
    else:
        article.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('articles:detail', args=[str(pk)]))

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryListView(request):
    cat_menu_list = Category.objects.all()   
    return render(request, 'articles/category_list.html', {'cat_menu_list':cat_menu_list})


def CategoryView(request, cats):
    category_articles = Article.objects.filter(category=cats.replace('-',' '))
    return render(request, 'articles/categories.html', {'cats':cats.title().replace('-',' '), 'category_articles':category_articles})

class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_detail.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Article, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class ArticleCreateView(CreateView):
    model = Article
    form_class = CreateArticle
    template_name = "articles/article_create.html"
    # fields = '__all__'

class ArticleCommentView(CreateView):
    model = Comment
    form_class = CommentArticle
    template_name = "articles/add_comment.html"
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('list') 


class ArticleCategoryView(CreateView):
    model = Category
    #form_class = CreateArticle
    template_name = "articles/article_category.html"
    fields = '__all__'

class EditUpdateView(UpdateView):
    model = Article
    form_class = EditArticle
    template_name = 'articles/edit.html'
    #fields=["title","year","slug","body","thumb", "author"]

class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('list') 
