from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank,  TrigramSimilarity
from django.shortcuts import render
from .forms import SearchForm
from post.models import Post

def post_search(request):
    form = SearchForm()
    query = None

    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():

            query = form.cleaned_data['query']

            # results = Post.published.annotate(search=SearchVector('title', 'body')).filter(search=query)
            # search_vector = SearchVector('title', weight='A') + \
            #                 SearchVector('body', weight='B')
            # search_query = SearchQuery(query)
            # results = Post.published.annotate(
                                        # rank=SearchRank(search_vector, search_query)
                                        # ).filter(rank__gte=0.3).order_by('-rank')
            results = Post.published.annotate(similarity=TrigramSimilarity('title', query),
                                                ).filter(similarity__gt=0.1).order_by('-similarity')
            print(results)
    return render(request, 'search/search.html',{'query': query,
                                                'form': form,
                                                'results': results})