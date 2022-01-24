from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('profile/', include('users.urls', namespace='users_profile')), 
    path('search/', include('search.urls', namespace='search')), 
    path('accounts/', include('allauth.urls')),

    path('', include('post.urls', namespace='post')),

]

