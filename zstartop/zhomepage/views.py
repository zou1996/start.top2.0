from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from zhomepage.models import Article,People,Comment
from zhomepage.form import CommentForm
# Create your views here.


def homepage(request):
    context = {}
    index_homepage = render(request,"myblog2.0.html",context)
    return index_homepage


def blog(request):
    queryset = request.GET.get('tag')
    if queryset:
        article_list = Article.objects.filter(tag=queryset)
    else:
        article_list = Article.objects.all()
    context = {}
    context['article_list'] = article_list
    index_blog = render(request,"blog.html",context)
    return index_blog

def yyy(request):
    context = {}
    index_yyy = render(request,"yyy.html",context)
    return index_yyy

# def detail(request,pk):
#     if request.method == 'GET':
#         form = CommentForm
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             comment = form.cleaned_data['comment']
#             c = Comment(name=name,comment=comment)
#             c.save()
#             return redirect(to='detail')
#     context = {}
#     comment_list = Comment.objects.all()
#     context['comment_list'] = comment_list
#     context['form'] = form
#     post = get_object_or_404(Post, pk=pk)
#     index_detail = render(request,"detail.html",context={'post':post})
#     return index_detail
def detail(request, page_num, error_form=None):
    context = {}
    form = CommentForm
    a = Article.objects.get(id=page_num)
    best_comment = Comment.objects.filter(best_comment=True, belong_to=a)
    if best_comment:
        context['best_comment'] = best_comment[0]
    article = Article.objects.get(id=page_num)
    context['article'] = article
    # context['comment_list'] = comment_list
    if error_form is not None:
        context['form'] = error_form
    else:
        context['form'] = form
    return render(request, 'detail.html', context)

def detail_comment(request, page_num):
    form = CommentForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        a = Article.objects.get(id=page_num)
        c = Comment(name=name, comment=comment, belong_to=a)
        c.save()
    else:
        return detail(request, page_num, error_form=form)

    return redirect(to='detail', page_num=page_num)


def msgboard(request):
    if request.method == 'GET':
        form = CommentForm
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            c = Comment(name=name,comment=comment)
            c.save()
            return redirect(to='msgboard')
    context = {}
    comment_list = Comment.objects.all()
    context['comment_list'] = comment_list
    context['form'] = form
    index_msgboard = render(request,"msgboard.html",context)
    return index_msgboard
