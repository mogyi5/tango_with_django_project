from django.contrib import admin
from rango.models import Category, Page
#from rango.models import Recipe, Ingredient, Review
from rango.models import UserProfile

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
	list_display = ('title','category','url')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

#----------------------------------------------------
# this is ours below, we dont need to look at ingredients or reviews individually right
# just looking at the recipes and users
# class RecipeAdmin(admin.ModelAdmin):
# 	prepopulated_fields = {'slug':('title',)}
#
# admin.site.register(Recipe, RecipeAdmin)
# admin.site.register(UserProfile)

# Register your models here.
