from django.db import models
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    description = models.TextField()
    url = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/')  # Assuming you're using the Django file upload feature

    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.name} - {self.email}'


class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    comment = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    rating = models.PositiveIntegerField(default=5)

    def __str__(self):
        return f'Testimonial by {self.name}'