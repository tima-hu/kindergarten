from django.db import models


class Kindergarten(models.Model):
    name = models.CharField("Название садика", max_length=200)
    slogan = models.CharField("Слоган", max_length=250, blank=True)
    about = models.TextField("О садике", blank=True)
    founded_year = models.PositiveIntegerField("Год основания", null=True, blank=True)
    students_count = models.PositiveIntegerField("Сейчас обучаются (детей)", default=0)
    graduates_count = models.PositiveIntegerField("Всего выпущено (детей)", default=0)
    groups_count = models.PositiveIntegerField("Количество групп", default=0)

    founder_name = models.CharField("Учредитель", max_length=200, blank=True)
    founder_info = models.TextField("Об учредителе", blank=True)
    director_name = models.CharField("Директор", max_length=200, blank=True)
    director_info = models.TextField("О директоре", blank=True)
    director_photo = models.ImageField("Фото директора", upload_to="director/", blank=True)

    address = models.CharField("Адрес", max_length=250, blank=True)
    phone = models.CharField("Телефон", max_length=100, blank=True)
    email = models.EmailField("E-mail", blank=True)
    working_hours = models.TextField("График работы садика", blank=True,
                                     help_text="Каждая строка с новой строки, например: Пн–Пт: 7:30–18:30")
    license_info = models.CharField("Лицензия / документы", max_length=250, blank=True)
    extra_info = models.TextField("Прочая информация (питание, кружки, правила)", blank=True)

    class Meta:
        verbose_name = "Информация о садике"
        verbose_name_plural = "Информация о садике"

    def __str__(self):
        return self.name


class Teacher(models.Model):
    full_name = models.CharField("ФИО", max_length=200)
    position = models.CharField("Должность", max_length=150, default="Воспитатель")
    group = models.CharField("Группа", max_length=100, blank=True)
    experience = models.CharField("Стаж / образование", max_length=200, blank=True)
    photo = models.ImageField("Фото", upload_to="teachers/", blank=True)
    schedule = models.TextField("График работы", blank=True,
                                help_text="Каждый день с новой строки, например: Пн, Ср, Пт: 7:30–15:30")
    phone = models.CharField("Телефон", max_length=100, blank=True)
    order = models.PositiveIntegerField("Порядок показа", default=0)
    is_active = models.BooleanField("Показывать на сайте", default=True)

    class Meta:
        ordering = ["order", "full_name"]
        verbose_name = "Воспитатель / сотрудник"
        verbose_name_plural = "Воспитатели и сотрудники"

    def __str__(self):
        return self.full_name
