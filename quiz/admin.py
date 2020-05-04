from django.contrib import admin

from .models import Quiz, Question, Category

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Category)
