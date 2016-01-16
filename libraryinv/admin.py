from django.contrib import admin
from .models import Location, Publisher, Publication, Line, Invoice
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class PublisherResource(resources.ModelResource):

    class Meta:
        model = Publisher


class PublisherAdmin(ImportExportModelAdmin):
    resource_class = PublisherResource
    pass


class PublicationResource(resources.ModelResource):

    class Meta:
        model = Publication


class PublicationAdmin(ImportExportModelAdmin):
    resource_class = PublicationResource
    pass

admin.site.register(Publication, PublicationAdmin)
admin.site.register(Location)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Line)
admin.site.register(Invoice)

