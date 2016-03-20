from django.contrib import admin
from sysrev.models import *


# Add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Update the registeration to include this customised interface
#admin.site.register(Category, CategoryAdmin)
#admin.site.register(Page)

admin.site.register(Researcher)
admin.site.register(Review)
admin.site.register(Paper)
# admin.site.register(Query)