from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

class Country(models.Model):
    country_name = models.CharField(max_length=80)
    country_code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.country_name}, {self.country_code}"

class Address(models.Model):
    street = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"

    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    address = models.OneToOneField(Address, on_delete=models.CASCADE,null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # author = models.CharField(default="default", max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')
    is_best_selling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    published_countries = models.ManyToManyField(Country)
    
    def get_absolute_url(self):
        return reverse("book-details", args=[self.slug])
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.title}({self.rating}) by {self.author}. best selling: {self.is_best_selling})"

