from django.shortcuts import render
from haystack.query import SearchQuerySet
from .models import Post
from .search_indexes import PostIndex

# Create your views here.
def post_list(request):
    #sqs = SearchQuerySet().all()
    #print(sqs.count())






    # qs = Post.objects.all()
    #
    q = request.GET.get('q', '')
    #
    # if q:
    #     results = SearchQuerySet().filter(content=q)
    #     for t in results:
    #         print(t.author)
    #         print(t.text)

    suggestedSearchTerm = SearchQuerySet().spelling_suggestion(q)
    print(suggestedSearchTerm)

    results = SearchQuerySet().models(Post).filter(content=q)
    for t in results:
        #print(t.author)
        print(t.text)
        #print(t.suggestions)

    return render(request, 'blogg/post_list.html',{
        #results : 'results',
    })

