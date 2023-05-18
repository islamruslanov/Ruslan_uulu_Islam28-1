from django.contrib import admin
from posts.models import Post,Product,Review
# Register your models here.

admin.site.register(Post)
admin.site.register(Product)
admin.site.register(Review)