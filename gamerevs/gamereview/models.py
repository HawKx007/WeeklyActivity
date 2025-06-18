from django.db import models
from django.template.defaultfilters import slugify


class Tags(models.Model):
    label = models.CharField(max_length=20)

    def __str__(self):
        return self.label


class Developer(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)
    label_tags = models.ManyToManyField(Tags)
    slug = models.SlugField(max_length=150, unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)

    def save(self, *args, **kwargs):
        creating = self.pk is None
        super().save(*args, **kwargs)
        if creating:
            self.slug = f'{self.pk}-{slugify(self.game.title)}'
            self.save(update_fields=['slug'])

    def __str__(self):
        return f"Review of {self.game.title}"
