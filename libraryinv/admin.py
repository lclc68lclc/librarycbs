from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Location, Publisher, Publication, Line, Invoice


admin.site.register(Publication)
admin.site.register(Location)
admin.site.register(Publisher)
admin.site.register(Line)
admin.site.register(Invoice)