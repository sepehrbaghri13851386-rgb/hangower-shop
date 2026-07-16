from django.db import connection
from django.db.migrations.recorder import MigrationRecorder

with connection.cursor() as cursor:
    cursor.execute("DROP TABLE IF EXISTS cart_app_cartitem;")
    cursor.execute("DROP TABLE IF EXISTS cart_app_cart;")

MigrationRecorder.Migration.objects.filter(app='cart_app').delete()

with connection.cursor() as cursor:
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'cart_app%';")
    print("جدول‌های باقی‌مانده:", cursor.fetchall())

print("پاکسازی تمام شد")