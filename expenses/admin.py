from django.contrib import admin
from .models import Expense,Tag
from django.contrib.staticfiles.storage import staticfiles_storage

# Register your models here.

class TagInLine(admin.TabularInline):
    model=Tag
    extra=1
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title','amount','category','date')
    search_fields = ('title','category')
    list_filter=('category','date')
    ordering=('-date','title',)
    inlines=[TagInLine]