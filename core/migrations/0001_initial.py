from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Kindergarten",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200, verbose_name="Название садика")),
                ("slogan", models.CharField(blank=True, max_length=250, verbose_name="Слоган")),
                ("about", models.TextField(blank=True, verbose_name="О садике")),
                ("founded_year", models.PositiveIntegerField(blank=True, null=True, verbose_name="Год основания")),
                ("students_count", models.PositiveIntegerField(default=0, verbose_name="Сейчас обучаются (детей)")),
                ("graduates_count", models.PositiveIntegerField(default=0, verbose_name="Всего выпущено (детей)")),
                ("groups_count", models.PositiveIntegerField(default=0, verbose_name="Количество групп")),
                ("founder_name", models.CharField(blank=True, max_length=200, verbose_name="Учредитель")),
                ("founder_info", models.TextField(blank=True, verbose_name="Об учредителе")),
                ("director_name", models.CharField(blank=True, max_length=200, verbose_name="Директор")),
                ("director_info", models.TextField(blank=True, verbose_name="О директоре")),
                ("director_photo", models.ImageField(blank=True, upload_to="director/", verbose_name="Фото директора")),
                ("address", models.CharField(blank=True, max_length=250, verbose_name="Адрес")),
                ("phone", models.CharField(blank=True, max_length=100, verbose_name="Телефон")),
                ("email", models.EmailField(blank=True, max_length=254, verbose_name="E-mail")),
                ("working_hours", models.TextField(blank=True, help_text="Каждая строка с новой строки, например: Пн–Пт: 7:30–18:30", verbose_name="График работы садика")),
                ("license_info", models.CharField(blank=True, max_length=250, verbose_name="Лицензия / документы")),
                ("extra_info", models.TextField(blank=True, verbose_name="Прочая информация (питание, кружки, правила)")),
            ],
            options={"verbose_name": "Информация о садике", "verbose_name_plural": "Информация о садике"},
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=200, verbose_name="ФИО")),
                ("position", models.CharField(default="Воспитатель", max_length=150, verbose_name="Должность")),
                ("group", models.CharField(blank=True, max_length=100, verbose_name="Группа")),
                ("experience", models.CharField(blank=True, max_length=200, verbose_name="Стаж / образование")),
                ("photo", models.ImageField(blank=True, upload_to="teachers/", verbose_name="Фото")),
                ("schedule", models.TextField(blank=True, help_text="Каждый день с новой строки, например: Пн, Ср, Пт: 7:30–15:30", verbose_name="График работы")),
                ("phone", models.CharField(blank=True, max_length=100, verbose_name="Телефон")),
                ("order", models.PositiveIntegerField(default=0, verbose_name="Порядок показа")),
                ("is_active", models.BooleanField(default=True, verbose_name="Показывать на сайте")),
            ],
            options={"verbose_name": "Воспитатель / сотрудник", "verbose_name_plural": "Воспитатели и сотрудники", "ordering": ["order", "full_name"]},
        ),
    ]
