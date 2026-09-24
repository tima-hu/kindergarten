from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

admin.site.site_header = "Управление сайтом детского сада"
admin.site.site_title = "Детский сад"
admin.site.index_title = "Что редактируем?"

urlpatterns = [
    path("admin/", admin.site.urls),
    # Загруженные через админку фото. На VPS их быстрее отдаёт nginx, но и без него всё работает.
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    path("", include("core.urls")),
]
