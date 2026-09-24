# Публикация сайта

## Вариант A: свой сервер (VPS, Ubuntu 22.04/24.04)
1. Домен направьте A-записью на IP сервера.
2. Загрузите папку проекта на сервер в `/var/www/kindergarten` (через `scp -r`, WinSCP или git).
3. Выполните:
   ```bash
   sudo bash /var/www/kindergarten/deploy/deploy.sh ваш-домен.ru
   sudo -u www-data /var/www/kindergarten/venv/bin/python /var/www/kindergarten/manage.py createsuperuser
   ```
   Скрипт сам поставит nginx и gunicorn, создаст `.env` со случайным ключом, соберёт статику и запустит сайт. Он открывается и по IP, и по домену.
4. HTTPS: `apt install -y certbot python3-certbot-nginx && certbot --nginx -d ваш-домен.ru -d www.ваш-домен.ru`, затем в `.env` поставьте `HTTPS=True` и выполните `systemctl restart kindergarten`.

Обновление после правок кода: загрузить файлы, затем
```bash
cd /var/www/kindergarten && venv/bin/pip install -r requirements.txt && venv/bin/python manage.py migrate && venv/bin/python manage.py collectstatic --noinput && chown -R www-data:www-data . && systemctl restart kindergarten
```

Резервная копия: файл `db.sqlite3` и папка `media/`. Копируйте их регулярно.

## Вариант B: PythonAnywhere
1. Загрузите проект, в консоли: `python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`.
2. Создайте `.env` по образцу `.env.example` (ALLOWED_HOSTS: `логин.pythonanywhere.com`).
3. `python manage.py migrate && python manage.py collectstatic --noinput && python manage.py createsuperuser`.
4. Вкладка Web: Manual configuration, укажите путь к venv, в WSGI-файле добавьте путь проекта и `DJANGO_SETTINGS_MODULE=config.settings`.
5. Static files: URL `/static/` → `<проект>/staticfiles`. Фото отдаёт сам Django.

## Локальная разработка
Создайте `.env` с `DEBUG=True`, затем `python manage.py runserver`.
