from django.db import models
from django.template.defaultfilters import slugify
from transliterate import translit


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            translit_list = Category.objects.filter(name=translit(self.name, 'ru', reversed=True))
            if translit_list:
                self.slug = slugify(translit(self.name, 'ru', reversed=True)) + "-" + str(len(translit_list) + 1)
            else:
                self.slug = slugify(translit(self.name, 'ru', reversed=True))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
