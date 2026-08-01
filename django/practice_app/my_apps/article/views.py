from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . import models
from django.db.models.functions import Length
from django.http import HttpResponse

# render home app
def home_view(request):
    return render(request, 'article_app/home.html')

#helper functions & datas
#data for filtering
data = {
        'title_data' : "article 2",
        'title_data2':"example",
        'author' : "fahim abrar",
        'suffix' : 'ex',
        'year' : 2026,
        'author_email':'artipeai@gmail.com',
}

def render_articles(request, queryset):
    return render(
        request, 'article_app/show_arts.html', #html page rendering
        {
            'data':queryset
        }
    )

def filter_helper(request, filter_name):

    if request.method == "GET":
        if filter_name == "exact":
            articles = models.Article.objects.filter(title__exact=data['title_data'])
            return render_articles(request,articles)
        
        elif filter_name == "author":
             articles = models.Article.objects.filter(author__icontains=data['author'])
             return render_articles(request,articles)
        
        elif filter_name == "year":
             articles = models.Article.objects.filter(created_at__year = data['year'])
             return render_articles(request,articles)
        
        elif filter_name == "without_title":
            articles = models.Article.objects.exclude(title__contains=data['title_data'])
            return render_articles(request,articles)
        
        elif filter_name == "chain_filter":
            articles = models.Article.objects.filter(author__icontains=data['author']).exclude(author_email__contains=data['author_email'])
            return render_articles(request,articles)
        
        elif filter_name == "iexact_filter":
             articles = models.Article.objects.filter(title__iexact=data['title_data2'])
             return render_articles(request,articles)
        
        elif filter_name == "startswith_filter":
            articles = models.Article.objects.filter(title__startswith=data['suffix'])
            return render_articles(request,articles)
        
        elif filter_name == "title_gt_3":
             articles = models.Article.objects.annotate(
                 title_len = Length("title")
             ).filter(title_len=4)

             return render_articles(request,articles)
        
    return render(request, 'article_app/show_arts.html')


# show all articles
def show_articles(request):
    # কন্ডিশনের বাইরে সরাসরি রাখা ভালো যাতে যেকোনো রিকোয়েস্টে ভেরিয়েবলটি ডেটা পায়
    articles = models.Article.objects.all()
    return render_articles(request,articles)

# create new article
def create_article(request):
    if request.method == "POST":
        title = request.POST.get('title')
        category = request.POST.get('category')
        content = request.POST.get('content')

        # Author info and file data
        author_name = request.POST.get('author_name')
        author_email = request.POST.get('author_email')
        author_image = request.FILES.get('author')
        document = request.FILES.get('document_data')

        # creating an instance of Article model
        models.Article.objects.create(
            title=title,
            category=category,
            content=content,
            author=author_name,
            author_email=author_email,
            author_image=author_image,
            document_file=document,
        )

        messages.success(request, f"{title} আর্টিকেলটি সফলভাবে তৈরি হয়েছে!")
        # ফর্ম সাবমিট হওয়ার পর রিডাইরেক্ট করা হলো (PRG Pattern)
        return redirect('show_articles') # 'show_articles' এর জায়গায় আপনার urls.py এর nameটি দিন
        
    return render(request, 'article_app/create.html')

# update an article
def update_article(request, pk):
    # get_object_or_404 ব্যবহার করলে আইডি না থাকলে ৪MD৪ দেখাবে, সাইট ক্র্যাশ করবে না
    article = get_object_or_404(models.Article, id=pk)

    if request.method == "POST":
        article.title = request.POST.get('title')
        article.category = request.POST.get('category')
        article.content = request.POST.get('content')
        article.author_email = request.POST.get('author_email')
        
        # আপনার ক্রিয়েট ভিউয়ের মডেল ফিল্ড অনুযায়ী নামগুলো ফিক্স করা হলো
        article.author = request.POST.get('author_name') 
       
        if request.FILES.get('author'):
            article.author_image = request.FILES.get('author')
        
        if request.FILES.get('document_data'):
            article.document_file = request.FILES.get('document_data')
    
        # saving changes
        article.save()

        messages.success(request, "Article updated successfully!")
        # আপডেটের পর রিডাইরেক্ট
        return redirect('show_articles')

    return render(request, 'article_app/update.html', {'data': article})

# delete an article
def delete_article(request, pk):
    article = get_object_or_404(models.Article, id=pk)
    
    # ইউজার যখন ডিলিট পেজে এসে "Confirm Delete" বাটনে চাপ দেবে (POST রিকোয়েস্ট)
    if request.method == "POST":
        article.delete()
        messages.warning(request, "Article deleted successfully!")
        return redirect('show_articles')
        
    # GET রিকোয়েস্টে ডিলিট কনফার্মেশন পেজ দেখাবে
    return render(request, 'article_app/delete.html', {'data': article})


# search and filters
def search_article(request):
    search_query = request.GET.get("query")

    articles = models.Article.objects.filter(
        title__icontains=search_query
    ) if search_query else models.Article.objects.all()

    return render_articles(request,articles)

#filters practice
#filter()
def exact_filter(request):   
    return filter_helper(request, "exact")
    
def filter_by_author(request):
    return filter_helper(request, "author")

def filter_by_year(request):
    return filter_helper(request, "year")

#exclude()
def filter_without_title(request):
    return filter_helper(request, "without_title")

#chaining filter() => exclude()
def filter_by_author_email(request):
    return filter_helper(request, "chain_filter")

#__iexact filter only get data if query matches
def filter_iexact_title(request):
    return filter_helper(request, "iexact_filter")

#startswith filter
def filter_startswith_suffix(request):
    return filter_helper(request, "startswith_filter")

#article len(title) > 3
def filter_by_title_len_gt(request):
    return filter_helper(request, "title_gt_3")


  