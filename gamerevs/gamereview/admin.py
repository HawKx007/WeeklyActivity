from django.contrib import admin
from .models import Game, Review, Tags, Developer


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'developer', 'platform')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'developer__name')
    list_filter = ('platform', 'label_tags')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('game', 'review', 'date')
    readonly_fields = ('date',)
    search_fields = ('game__title', 'review')
    prepopulated_fields = {'slug': ('game',)}  # optional, auto-editable


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('label',)
    search_fields = ('label',)


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
    search_fields = ('name',)
