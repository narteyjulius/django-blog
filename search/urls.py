from django.urls import path
from .views import SearchResultsList

app_name = 'search'

urlpatterns = [

    path('', SearchResultsList.as_view(), name='post_search'),

]

