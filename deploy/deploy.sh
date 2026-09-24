#!/usr/bin/env bash
# Установка на чистый Ubuntu 22.04/24.04. Запуск от root:
#   sudo bash deploy/deploy.sh ваш-домен.ru
# Проект должен лежать в /var/www/kindergarten
set -euo pipefail
DOMAIN="${1:?Укажите домен: sudo bash deploy/deploy.sh example.com}"
APP=/var/www/kindergarten
cd "$APP"

apt-get update
apt-get install -y python3-venv python3-pip nginx

python3 -m venv venv
venv/bin/pip install --upgrade pip
venv/bin/pip install -r requirements.txt

if [ ! -f .env ]; then
  IP=$(hostname -I | awk '{print $1}')
  KEY=$(python3 -c "import secrets; print(secrets.token_urlsafe(50))")
  cat > .env <<ENV
SECRET_KEY=$KEY
DEBUG=False
ALLOWED_HOSTS=$DOMAIN,www.$DOMAIN,$IP
CSRF_TRUSTED_ORIGINS=http://$DOMAIN,https://$DOMAIN,http://www.$DOMAIN,https://www.$DOMAIN,http://$IP
HTTPS=False
ENV
fi

mkdir -p media
venv/bin/python manage.py migrate --noinput
venv/bin/python manage.py collectstatic --noinput
chown -R www-data:www-data "$APP"

cp deploy/kindergarten.service /etc/systemd/system/kindergarten.service
systemctl daemon-reload
systemctl enable --now kindergarten
systemctl restart kindergarten

sed "s/DOMAIN/$DOMAIN/g" deploy/nginx.conf > /etc/nginx/sites-available/kindergarten
ln -sf /etc/nginx/sites-available/kindergarten /etc/nginx/sites-enabled/kindergarten
rm -f /etc/nginx/sites-enabled/default
nginx -t && systemctl reload nginx

echo
echo "Готово. Осталось:"
echo "  1) cd $APP && sudo -u www-data venv/bin/python manage.py createsuperuser"
echo "  2) Включить HTTPS: apt install -y certbot python3-certbot-nginx && certbot --nginx -d $DOMAIN -d www.$DOMAIN"
echo "  3) В $APP/.env поставить HTTPS=True и выполнить: systemctl restart kindergarten"
