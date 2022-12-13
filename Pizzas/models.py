from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='img', blank=True, null=True, height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'topping'

    def __str__(self):
        return self.topping_name

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class Meta:
        verbose_name_plural = 'comments'

def __str__(self) :
    return f"{self. text [:50]}..."

