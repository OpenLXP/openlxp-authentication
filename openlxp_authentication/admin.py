from django.contrib import admin
from .models import SAMLConf


@admin.register(SAMLConf)
class SAMLConfAdmin(admin.ModelAdmin):
    list_display = ('name', 'entity_id',)
