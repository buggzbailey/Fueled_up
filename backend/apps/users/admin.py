from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from django.db.models import fields
from .models import User
# Register your models here.
@admin.register(User)
class UserModel(admin.ModelAdmin):
    fields = ['user_name','email','token','token_expires_at']
    list_filter = []
    list_display = fields
    search_feilds = ['user_name','email']