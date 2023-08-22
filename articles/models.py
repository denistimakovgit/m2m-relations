from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name="Категория")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    category = models.ManyToManyField(Category, through='Scope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Scope(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scope')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='scope')
    main_flag = models.BooleanField()

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематика статьи'
        #ordering = ['-main_flag', 'category__category_name']