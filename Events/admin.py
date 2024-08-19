from django.contrib import admin
from .models import Event, Message, Subscription, Testimonial

admin.site.register(Event)
admin.site.register(Message)
admin.site.register(Subscription)
admin.site.register(Testimonial)
