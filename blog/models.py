# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

STATUS_CHOICES = (
    (0, "Draft"),
    (1, "Published")
)

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='tag_icons/', blank=True, null=True)

    #class to control the plural name of the class
    class Meta:
        verbose_name_plural = 'tags'

    #provide a better string representation of your objects
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True, editable=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    tags = models.ManyToManyField(Tag, related_name='posts')
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)  
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    views_count = models.PositiveIntegerField(default=0)  # Add this field to track views
    reading_time = models.PositiveIntegerField(default=1)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)