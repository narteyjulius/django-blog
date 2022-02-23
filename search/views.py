from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank,  TrigramSimilarity
from post.models import Post
from django.db.models import Q
from django.views.generic.list import ListView


class SearchResultsList(ListView):
    model = Post
    context_object_name = "results"
    template_name = "search/search.html"

    def get_queryset(self):
        query = self.request.GET.get("query")
        search_vector = SearchVector("title", "body")
        search_query = SearchQuery(query)

        return (
            Post.objects.annotate(
                search=search_vector, rank=SearchRank(search_vector, search_query)
            )
            .filter(search=search_query)
            .order_by("-rank")
        )

        # return Post.objects.filter(title__search=query)
