from django.shortcuts import render
from haystack.query import SearchQuerySet
from .models import Post

# Create your views here.
def post_list(request):
    sqs = SearchQuerySet().all()
    print(sqs.count())

    results = SearchQuerySet().filter(content='hello')
    for t in results:
        print(t.author)
        print(t.text)

    return render(request, 'blogg/post_list.html')