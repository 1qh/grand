from django.contrib import admin

from .models import Room, Topic, Comment

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Comment)
