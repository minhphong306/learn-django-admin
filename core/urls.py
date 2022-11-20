from django.contrib import admin
from django.urls import path
from blog.admin import blog_site

urlpatterns = [
    path('blogadmin/', blog_site.urls),
]

admin.site.index_title = "Bookstore system index_title"
admin.site.site_header = "Bookstore system site_header"
admin.site.site_title = "Bookstore system site_title"
