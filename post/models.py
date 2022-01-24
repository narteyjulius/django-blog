from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class PublishedManager(models.Manager):
        def get_queryset(self):
            return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
                        ('draft', 'Draft'),
                        ('published', 'Published'),
    )
    FEATURED_CHOICES = (
                        ('true', 'True'),
                        ('false', 'False'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = RichTextUploadingField(blank=True, null=True, config_name='special')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='blog_pics', blank=True, null=True, default='media/no_image.png')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post:post_detail',
                                        args=[self.publish.year,
                                        self.publish.month,
                                        self.publish.day, self.slug])

    def save(self, *args, **kwargs):
        if self.is_featured:
            try:
                temp = Post.objects.get(is_featured=True)
                if self != temp:
                    temp.is_featured = False
                    temp.save()
            except Post.DoesNotExist:
                pass
        
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    STATUS_CHOICES = (
                        ('true', 'True'),
                        ('false', 'False'),
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='commet_img', blank=True, null=True, default='media/default.jpg')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'                                      