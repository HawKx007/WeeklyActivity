from django.db import models
from django.template.defaultfilters import slugify

class Tags(models.Model):
    label = models.CharField(max_length=20)

    def __str__(self):
        return self.label


class Game(models.Model):
    title = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    platform = models.CharField(max_length=50, default='null')
    label_tags = models.ManyToManyField(Tags)
    slug = models.SlugField(max_length=150, default='null', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=150, default='null', blank=True)
    id: int

    def save(self, *args, **kwargs):
        if not self.id:
            # Save first to generate the ID
            super().save(*args, **kwargs)
        self.slug = f'{self.id}-{slugify(self.game.title)}'
        super().save(update_fields=['slug'])

    def __str__(self):
        return f"Review of {self.game.title}"
