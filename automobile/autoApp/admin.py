from django.contrib import admin
from .models import Fix, Manufacturer, ManufactureWorkSpace, WorkSpace, Automobile


# Register your models here.

class AdminFix(admin.ModelAdmin):
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(AdminFix, self).save_model(request, obj, form, change)


class ManufacurerWorkspaceAdmin(admin.TabularInline):
    model = ManufactureWorkSpace
    extra = 1


class AdminWorkSpace(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    inlines = [ManufacurerWorkspaceAdmin, ]


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False


class AdminCar(admin.ModelAdmin):
    list_display = ('type', 'max_speed',)


admin.site.register(Fix, AdminFix)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(WorkSpace, AdminWorkSpace)
admin.site.register(Automobile, AdminCar)
