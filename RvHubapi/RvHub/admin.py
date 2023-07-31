from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(CandidateInfo)
class CandidateInfoAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display=[field.name for field in CandidateInfo._meta.get_fields()]
    