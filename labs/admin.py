from django.contrib import admin
from .models import Lab, Skill


@admin.register(Lab)
class LabAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'skill', 'publish',   
                       'status')
    list_filter = ('skill', 'status', 'created', 'publish', 'author')
    search_fields = ('title', 'skill')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author', 'skill')
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass