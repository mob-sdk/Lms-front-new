from django.contrib import admin

# Register your models here.
from .models import Comment, CommentMultip
 
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_time']
    fields = ['name', 'text', 'post']
 
class CommentMultipAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'commentobject', 'created_time','parent']
    fields = ['name', 'text', 'commentobject','parent']
 
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentMultip, CommentMultipAdmin)