from django.contrib import admin
from .models import course
# Register your models here.
class courseAdmin(admin.ModelAdmin):
    list_display = ('title', 'Link', 'created_at')
admin.site.register(course, courseAdmin)