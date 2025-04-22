from django.db import models

# Brand Model
class Brand(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    manufacturing_since = models.DateField()

    def __str__(self):
        return self.name

# Model (Phone Model)
class PhoneModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    launch_date = models.DateField()
    platform = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.brand.name} {self.model_name}"

# Review Model (Many-to-Many with PhoneModel)
class Review(models.Model):
    phone_models = models.ManyToManyField(PhoneModel)
    review_article = models.TextField()
    date_published = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review published on {self.date_published}"
