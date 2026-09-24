from django.contrib import admin

from .models import Kindergarten, Teacher


@admin.register(Kindergarten)
class KindergartenAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Главное", {"fields": ("name", "slogan", "about", "founded_year")}),
        ("Статистика", {"fields": ("students_count", "graduates_count", "groups_count")}),
        ("Учредитель", {"fields": ("founder_name", "founder_info")}),
        ("Директор", {"fields": ("director_name", "director_info", "director_photo")}),
        ("Контакты и график", {"fields": ("address", "phone", "email", "working_hours")}),
        ("Прочее", {"fields": ("license_info", "extra_info")}),
    )

    def has_add_permission(self, request):
        # Информация о садике это одна запись: её можно только редактировать
        return not Kindergarten.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("full_name", "position", "group", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("is_active", "position")
    search_fields = ("full_name", "group")
