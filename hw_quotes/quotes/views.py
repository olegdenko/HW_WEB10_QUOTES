import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from django.core.paginator import Paginator

from quotes.forms import AuthorForm, QuoteForm
from .models import Quote, Author, Tag
# from .utils import get_mongodb
# from .utils import get_postgresql

# Create your views here.


def main(request, page=1):
    top_tags = Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:10]
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.get_page(page)

    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page, 'top_tags': top_tags})


def author_detail(request, author_id):
    top_tags = Tag.objects.annotate(
        num_quotes=Count('quote')).order_by('-num_quotes')[:10]
    author = Author.objects.get(id=author_id)
    return render(request, 'quotes/author_detail.html', {'author': author, 'top_tags': top_tags})


def tag_quotes(request, tag):
    top_tags = Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:10]
    quotes_with_tag = Quote.objects.filter(tags__name=tag)
    return render(request, 'quotes/tag_quotes.html', context={'quotes': quotes_with_tag, 'tag': tag, 'top_tags': top_tags})


@login_required
def add_author(request):
    form = AuthorForm(instance=Author())
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=Author())
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect(to="quotes:root")
    return render(
        request,
        "quotes/add_author.html",
        context={"title": "Web 10 hw!", "form": form}
    )


@login_required
def add_quote(request):
    form = QuoteForm(instance=Quote())
    if request.method == "POST":
        form = QuoteForm(request.POST, instance=Quote())
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect(to="quotes:root")
    return render(
        request,
        "quotes/add_quote.html",
        context={"title": "Web 10 hw!", "form": form}
    )


@login_required
def logined_quotes(request, page=1):
    quotes = Quote.objects.filter(user=request.user).all()
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.get_page(page)
    return render(request, 'quotes/index.html', context={"title": "Web 10 hw!", 'quotes': quotes_on_page})


@login_required
def remove(request, pic_id):
    picture = Picture.objects.filter(pk=pic_id, user=request.user)
    try:
        os.unlink(os.path.join(settings.MEDIA_ROOT, str(picture.first().path)))
    except OSError as e:
        print(e)
    picture.delete()
    return redirect(to="app_hw_web10:pictures")


@login_required
def edit(request, pic_id):
    if request.method == 'POST':
        description = request.POST.get('description')
        Picture.objects.filter(pk=pic_id, user=request.user).update(
            description=description)
        return redirect(to="app_hw_web10:pictures")

    picture = Picture.objects.filter(pk=pic_id, user=request.user).first()
    return render(request, "app_hw_web10/edit.html", context={"title": "Web 10 hw!", "pic": picture, "media": settings.MEDIA_URL})
def login(request):
    return render(request, "user/signin.html", context={"title": "Web 10 hw!"})


def register(request):
    return render(
        request, "user/signup.html", context={"title": "Web 10 hw!"}
    )
# def main(request, page=1):
#     db = get_postgresql(DATABASES)
#     quotes = db.quotes.find()
#     per_page = 10
#     paginator = Paginator(list(quotes), per_page)
#     quotes_on_page = paginator.page(page)
#     # return render(request, 'quotes/index.html', context={})
#     return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})
