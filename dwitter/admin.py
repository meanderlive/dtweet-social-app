from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User,Group
from .models import Dweet, Profile , Favourite_pages
# class UserAdmin(admin.ModelAdmin):
#     model = User
#     # Only display the "username" field
#     fields = ["username"]



class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Dweet)
admin.site.register(Profile)
admin.site.register(Favourite_pages)



#admin.site.register(Profile)