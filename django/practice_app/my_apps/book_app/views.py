from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Author, Book


# Application route names used in templates for navigation
app_routes = {
    "add_op": "add_books",
    "remove_op": "remove_books",
    "set_op": "set_books",
    "clear_op": "clear_books",
    "all_op": "all_books",
    #filtering and searching route
    "show_authors":"all_authors",
    "filter_author1":"filter_author_by_name",
    "filter_author2":"filter_author_by_book"
}


# ----------------------------
# Helper Functions
# ----------------------------

def get_all_books_and_authors():
    """Return all authors and books."""
    return Author.objects.all(), Book.objects.all()


def get_author_book_ids(request):
    """Get selected author and book IDs from POST request."""
    author_id = request.POST.get("author")
    book_id = request.POST.get("book")
    return author_id, book_id


def get_author_and_book(author_id, book_id):
    """Return Author and Book objects or raise 404."""
    author = get_object_or_404(Author, id=author_id)
    book = get_object_or_404(Book, id=book_id)
    return author, book


def handle_rendering(request, template, context=None):
    """Render template with context."""
    return render(request, template, context or {})


# ----------------------------
# Views
# ----------------------------

def homeapp(request):
    messages.success(request, "Welcome to the Books App")

    return render(
        request,
        "books_app/home.html",
        {
            "routes": app_routes,
        },
    )


def add_books(request):
    authors, books = get_all_books_and_authors()

    if request.method == "POST":
        author_id, book_id = get_author_book_ids(request)

        if author_id and book_id:
            author, book = get_author_and_book(author_id, book_id)

            book.author.add(author)

            messages.success(
                request,
                f'"{book.name}" was added to "{author.name}" successfully!',
            )

    return handle_rendering(
        request,
        "books_app/add_books.html",
        {
            "authors": authors,
            "books": books,
        },
    )


def remove_books(request):
    books = Book.objects.all()

    if request.method == "POST":
        author_id, book_id = get_author_book_ids(request)

        if author_id and book_id:
            author, book = get_author_and_book(author_id, book_id)

            book.author.remove(author)

            messages.success(
                request,
                f'"{book.name}" was removed from "{author.name}" successfully!',
            )

    return render(
        request,
        "books_app/remove_books.html",
        {
            "books": books,
        },
    )


def set_books(request):
    authors, books = get_all_books_and_authors()

    if request.method == "POST":
        author_id, book_id = get_author_book_ids(request)

        if author_id and book_id:
            author, book = get_author_and_book(author_id, book_id)

            book.author.set([author])

            messages.success(
                request,
                f'"{book.name}" was updated with "{author.name}" successfully!',
            )

    return handle_rendering(
        request,
        "books_app/set_books.html",
        {
            "authors": authors,
            "books": books,
        },
    )


def clear_books(request):
    #getting all books data from db
    books = Book.objects.all()

    if request.method == "POST":
        book_id = request.POST.get("book")

        book = get_object_or_404(Book, id=book_id)

        if book.author.count() == 0:
            messages.error(request, f'"{book.name}" already has no authors assigned.')
        else:
            book.author.clear()
            messages.success(request, f'"{book.name}" authors cleared successfully!')

    return handle_rendering(
              request,
              "books_app/clear_books.html",
              {
                  "books": books,
              },
          )


def all_books(request):
    books = Book.objects.all()

    return render(
        request,
        "books_app/all_books.html",
        {
            "books":books
        }
    )

#filtering and object queries for books and authors
def show_all_authors(request):
    #getting all authors data from db
    authors = Author.objects.all()

    context = {
        "authors":authors,
    }
    return render(request, 'books_app/filtering_queries/all_authors.html', context)

def filtering_by_author_name(request):
    # Get name from POST or GET and perform a safe query
    author_name = request.POST.get('name') or request.GET.get('name')

    # default to empty queryset to avoid referencing an undefined variable
    author_qs = Author.objects.none()

    if author_name:
        # use icontains for a more flexible match
        author_qs = Author.objects.filter(name__iexact=author_name)
        if author_qs.exists():
            messages.success(request, "Author data fetched successfully!")
        else:
            messages.info(request, "No authors matched the given name.")

    return handle_rendering(
        request,
        "books_app/filtering_queries/filter_author.html",
        {
            "author": author_qs,
        },
    )

def filtering_by_book_name(request):
    #get book name from user
    book_name = request.POST.get('book')

     # default to empty queryset to avoid referencing an undefined variable
    book_qs = Book.objects.none()
    
    if book_name:
        # use icontains for a more flexible match
        book_qs = Book.objects.filter(name__iexact=author_name)
            if author_qs.exists():
                messages.success(request, "Author data fetched successfully!")
            else:
                messages.info(request, "No authors matched the given name.")

    return handle_rendering(
           request,
                "books_app/filtering_queries/filter_author_by_book.html",
    )



