from django.contrib import admin
from .models import *


# Register your models here.
class BendEventAdmin(admin.TabularInline):
    model = BendEvent
    extra = 1


class EventAdmin(admin.ModelAdmin):
    exclude = ('user', 'bends', 'participants')
    list_display = ('name', 'date')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(EventAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return obj and obj.user == request.user

    def has_delete_permission(self, request, obj=None):
        return obj and obj.user == request.user

    inlines = [BendEventAdmin, ]


class BendAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


admin.site.register(Event, EventAdmin)
admin.site.register(Bend, BendAdmin)
admin.site.register(BendEvent)
