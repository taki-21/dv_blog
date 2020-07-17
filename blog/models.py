from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name='カテゴリ名', max_length=40)
    color = models.CharField(verbose_name='色(16進数)',
                             max_length=7, default='#000000')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=40)
    thumbnail = models.ImageField(verbose_name='サムネイル', blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name='カテゴリ')
    lead_text = models.TextField(verbose_name='紹介文')
    main_text = models.TextField(verbose_name='本文')
    created_at = models.DateTimeField(verbose_name='作成日', default=timezone.now)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
