from django.contrib import admin
from .models import Topic, Comment

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('subject', 'get_author_first_name', 'category', 'date_posted')
    search_fields = ('subject', 'author__first_name', 'author__last_name')  
    list_filter = ('category', 'date_posted')  
    date_hierarchy = 'date_posted'  

    def get_author_first_name(self, obj):
        return obj.author.first_name

    get_author_first_name.short_description = 'Autor'  

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('topic', 'get_commentator_first_name', 'date_posted')
    search_fields = ('topic__subject', 'Commentator__first_name', 'Commentator__last_name')  
    list_filter = ('date_posted',)  
    
    def get_commentator_first_name(self, obj):
        return obj.Commentator.first_name

    get_commentator_first_name.short_description = 'Comentarista'  
