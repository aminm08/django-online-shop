from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth import get_user_model

from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('product title'))
    description = RichTextField(verbose_name=_('product description'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('product price'))
    active = models.BooleanField(default=True, verbose_name=_('is this product available'))

    date_time_created = models.DateTimeField(verbose_name=_('Creation date time'), default=timezone.now())
    date_time_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


class Comment(models.Model):
    RATING_CHOICES = (
        ('1', _('Very bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    )

    body = models.TextField(verbose_name=_('Comment text'))
    rating = models.CharField(choices=RATING_CHOICES, default='3', max_length=1, verbose_name=_('your score'))

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    active = models.BooleanField(default=True, verbose_name=_('is this comment active'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}:{self.get_rating_display()}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
