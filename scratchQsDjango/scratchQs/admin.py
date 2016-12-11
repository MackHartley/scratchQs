from django.contrib import admin

from .models import Category, Question, Answer, Community

# Registering models here

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Community)