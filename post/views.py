from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count
from taggit.models import Tag
from .models import Post, Comment
from .forms import CommentForm, ContactForm
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import PostForm
from django.contrib.auth.decorators import login_required



def error_404_page(request, exception):
    return render(request, "errors/404.html")

def error_500_page(request, *args, **argv):
    return render(request, "errors/500.html", status=500)


def about(request):
    return render(request, 'about/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send()
            messages.success(request, f' Thank You for your message. Will get in touch soon')

        return redirect('post:contact')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form':form})


def post_list(request, tag_slug=None):
    posts = Post.published.all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 2) # 3 posts in each page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'post/post_list.html', { 'tag':tag,
                                                    'post_list': posts,
                                                    'posts': posts})


# def home_page(request, tag_slug=None):
#     posts = Post.published.all()
#     # featured_post = Post.objects.get(is_featured=True)
#     featured_post = get_object_or_404(Post, is_featured=True)
#     print(featured_post)


#     tag = None
#     if tag_slug:
#         tag = get_object_or_404(Tag, slug=tag_slug)
#         posts = posts.filter(tags__in=[tag])


#     return render(request, 'post/home_page.html', { 
#                                                     'tag':tag,
#                                                     'post_list': posts,
#                                                     'posts': posts,
#                                                     'featured': featured_post
#                                                     })




def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)

    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid:
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            messages.success(request, f' Your comment will be reviewed and be approved. This is done to avoid spam. Thank You! ')
    else:
        comment_form = CommentForm()


    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]
    leates_posts = Post.published.all()

    return render(request, 'post/post_detail.html',
                                        {'post': post,
                                        'comments': comments,
                                        'new_comment':new_comment,
                                        'comment_form': comment_form,
                                        'similar_posts': similar_posts
                                        })




class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "body", "image", "tags"]
    template = 'blog/post_form.html'

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been created successfully.')
        return reverse_lazy("blog:post_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.slug = slugify(form.cleaned_data['title'])
        obj.save()
        print(obj)
        print(obj.body)
        return super().form_valid(form)



def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES
                                    )
        if form.is_valid:
            form_save = form.save(commit=False)
            form_save.author = request.user
            form_save.slug = slugify(form.cleaned_data['title'])
            form_save.save()
            print(form_save)
            messages.success(request, f' Your Post has been created ')

            return redirect('users:my_profile')
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html',{'form':form})


@login_required
def delete_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        post.delete()
        messages.success(request, f' Your Address has been delected ')
        return redirect("blog:post_list")
    return render(request, 'blog/post_confirm_delete.html', {'obj':post} )



def update_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid:
            form_save = form.save(commit=False)
            form_save.author = request.user
            form_save.slug = slugify(form.cleaned_data['title'])
            form_save.save()
            messages.success(request, f' Your Post  has been Edited ')
            return redirect('users:my_profile')
    else:
        post_update = PostForm(instance=post)

    return render(request, 'blog/post_form.html',{'form':post_update})



class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "body", "image", "tags"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been updated successfully.')
        return reverse_lazy("blog:post_list")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)



class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been deleted successfully.')
        return reverse_lazy("blog:post_list")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)     