from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='article_home'),
    path("show_articles/", views.show_articles, name="show_articles"),
    path("create/", views.create_article, name="create_article"),
    path("update/<int:pk>/", views.update_article, name="update_article"),
    path("delete/<int:pk>/", views.delete_article, name="delete_article"),
    path("search/",views.search_article, name="search_article"),

    #filters
    path("filter1/", views.exact_filter, name="my exact filter"),
    path("filter2/", views.filter_by_author, name="my author filter"),
    path("filter3/", views.filter_by_year, name="my year filter"),
    path("filter4/", views.filter_without_title, name="my without title filter"),
    path("filter5/", views.filter_by_author_email, name="my author email filter"),
    path("filter6/", views.filter_iexact_title, name="my iexact title filter"),
    path("filter7/", views.filter_startswith_suffix, name="my suffix title filter"),
    path("filter8/", views.filter_by_title_len_gt, name="my title gt  filter"),
]