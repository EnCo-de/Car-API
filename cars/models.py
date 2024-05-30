from django.db import models

class Manufacturer(models.Model):
    brand = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.brand


class Car(models.Model):
    category =      models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    manufacturer =  models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model_name =    models.CharField(max_length=100)
    descripion =    models.TextField(blank=True)
    time_created =  models.DateTimeField(auto_now_add=True)
    time_updated =  models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.model_name


# Passenger car classification
# We break down passenger vehicles into body styles (coupes, sedans, 
# hatchbacks, etc) and explain the basic characteristics of each type.
class Category(models.Model):
    title = models.CharField(max_length=50)
    definition = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        indexes = [
            models.Index(fields=["title"])
        ]
        verbose_name_plural = 'categories'