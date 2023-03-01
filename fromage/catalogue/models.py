from django.db import models

# Create your models here.

class Cheese(models.Model):
    name = models.CharField(max_length=255)
    strength = models.IntegerField()
    colour = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.country}"

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    dob = models.DateField()
    vegetarian = models.BooleanField()
    orders = models.ManyToManyField(Cheese, blank=True, null=True, related_name="orders") #blank=True, null=True makes it okay for this field to be empty

    def __str__(self):
        return f"{self.id}. {self.name}"
    

class Review(models.Model):
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE, null=True, blank=True)
    reviewer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    recommend = models.BooleanField()

    def __str__(self):
        return f"{self.cheese} - {self.rating} ({self.date})"
