# Сайт детского сада (Django, одна страница)

## Запуск
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
- Сайт: http://127.0.0.1:8000/
- Админ-панель: http://127.0.0.1:8000/admin/

## Что заполнить в админке
1. **Информация о садике**: название, слоган, статистика (сколько учатся / выпущено), учредитель, директор, контакты, график.
2. **Воспитатели и сотрудники**: добавляйте по одному, с фото и графиком работы. Порядок и видимость меняются прямо в списке.

Публикация на сервере: см. `DEPLOY.md`. Локально создайте `.env` с `DEBUG=True` (образец в `.env.example`).
