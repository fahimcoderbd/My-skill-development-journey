from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from . import models

# Create your views here.
url_routes = {
        'author_name':'/notes/author',
        'author_notes':'/notes/author_notes'
}

def notes_home(request):

    content = "<h1>Welcome to notes</h1>" \
              "<h2>This my db practice with this notes app</h2>" \
              "Here are routes => <br>" \
               f'<a href="{url_routes['author_name']}">Access author name</a> <br>' \
               f'<a href="{url_routes['author_notes']}">Access author notes</a>'
    
    return HttpResponse(content)

def show_author_name(request):
    note = get_object_or_404(models.notes, id=1)
    
    return HttpResponse("<h1 style='color:blue;'>Showing Author data:</h1>" \
                       f"<h2>Author:{note.author} , ID:{note.id}</h2>")

def get_article_from_author(request):
    author = get_object_or_404(models.Author, id=1)
    #showing author's all notes
    notes = author.notes.all()

    result_data = "Showing author's note"

    result_data = "".join(
         f"<h2>Title: {note.title}, <br> ID: {note.id}</h2>"
         for note in notes
    )

    return HttpResponse(
        result_data
    )
   