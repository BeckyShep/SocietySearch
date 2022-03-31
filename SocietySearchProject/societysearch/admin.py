from django.contrib import admin
from societysearch.models import SocietyPage, Reviews

# Register your models here.

# admin.site.register(Page, PageAdmin)
# admin.site.register(UserProfile)
admin.site.register(SocietyPage)


class SocietyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
