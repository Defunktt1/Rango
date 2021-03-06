from django.db import models
from django.template.defaultfilters import slugify
from transliterate import translit


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    '''def save(self, *args, **kwargs):
        returned_length = Category.objects.filter(name=self.name)
        if returned_length:
            self.slug = slugify(translit(self.name, 'ru', reversed=True)) + "-" + str(len(returned_length))
        else:
            self.slug = slugify(translit(self.name, 'ru', reversed=True))
        super().save(*args, **kwargs)
'''
    def save(self, *args, **kwargs):
        temp_slug = slugify(translit(self.name, 'ru', reversed=True))
        while Category.objects.filter(slug=temp_slug):
            self.slug = slugify(translit(self.name, 'ru', reversed=True)) + "-2"
            temp_slug = self.slug
        if not self.slug:
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
