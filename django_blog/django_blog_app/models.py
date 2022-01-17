from django.db import models
from django.db.models.deletion import PROTECT
from django.utils import timezone
import datetime

class Category(models.Model):
    """Categories"""

    name = models.CharField("Name of Category", max_length=255)
    created_at = models.DateTimeField("作成日", default=datetime.datetime.now())

    def __str__(self):
        return self.name

class Post(models.Model):
    """Articles"""

    title = models.CharField("Title", max_length=255)
    text = models.TextField("Input Box")
    created_at = models.DateTimeField("CREATED AT", default=datetime.datetime.now())
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Comment(models.Model):
    """Comments for blog"""

    name = models.CharField("Name", max_length=30, default="anonymous")
    text = models.TextField("Comments")
    post = models.ForeignKey(Post, verbose_name='related articles', on_delete=PROTECT)
    created_at = models.DateTimeField("created_at", default=timezone.now)

    def __str__(self):
        return self.text(10)