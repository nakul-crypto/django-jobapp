from django.contrib import admin

from app_1.models import Author, JobPost, Location, Skills

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'salary')
    list_filter =('date','expiry','salary')
    search_fields = ['title']
    search_help_text = "Write in your query and hit Enter"
    # fields = (('title', 'description'),'expiry')
    # exclude = ('title',)
    fieldsets = (
        ('Basic info', {
        'fields': ('title', 'description')
        }),
        ('More info', {
        'classes': ('collapse', 'wide'),
        'fields': ('expiry', 'salary')
        })
    )


admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)