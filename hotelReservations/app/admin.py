from django.contrib import admin

from .models import Room, EmployeeRoom, Employee, Reservation


# Register your models here.

class ReservationAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('code', 'room',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(ReservationAdmin, self).save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "room":
            kwargs["queryset"] = Room.objects.filter(isClean=True).all()
        return super(ReservationAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def has_change_permission(self, request, obj=None):
        if obj and (obj.user == request.user or Reservation.objects.filter(user=request.user,
                                                                           employer__job_position="Менаџер").exists() or Reservation.objects.filter(
            user=request.user, employer__job_position="Рецепционер").exists()):
            return True


class EmployeeRoomAdmin(admin.TabularInline):
    model = EmployeeRoom
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "employee":
            kwargs["queryset"] = Employee.objects.filter(job_position='Хигеничар').all()
        return super(EmployeeRoomAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'isClean',)
    inlines = [EmployeeRoomAdmin, ]

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        if obj and EmployeeRoom.objects.filter(room=obj, employee__job_position="Хигеничар").exists():
            return True


admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Employee)
admin.site.register(EmployeeRoom)
