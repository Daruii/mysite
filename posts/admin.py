from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display= ["__unicode__","content", "timestamp", "updated"]
	list_display_links=["__unicode__", "updated"]
	list_filter=["updated"]
	search_fields=["title", "content"]
	list_editable=["content"]

	class Meta:
		model=Post

admin.site.register(Post, PostModelAdmin)