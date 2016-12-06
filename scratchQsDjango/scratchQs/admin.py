from django.contrib import admin

from .models import Question, Answer

# Registering models here

admin.site.register(Question)
admin.site.register(Answer)