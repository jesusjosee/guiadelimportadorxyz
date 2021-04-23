from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):

    STATUS_CHOICES = (
        ('draf', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=100, verbose_name="Título")
    slug = models.SlugField(max_length=100, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "blog_post")
    body = RichTextField(verbose_name="Contenido del Post")
    publish = models.DateTimeField(default=timezone.now, verbose_name="Fecha de publicación")
    status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=10)
    image = models.ImageField(verbose_name="Imagen", blank=True, null=True, upload_to='posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    #manager
    objects = models.Manager() #default
    published = PublishedManager() #our custom manager

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=[self.publish.year, self.publish.month, self.publish.day, 
                                                self.slug])