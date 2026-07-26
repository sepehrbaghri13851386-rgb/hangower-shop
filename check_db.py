import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_project.settings')
django.setup()

from django.db import connection

cursor = connection.cursor()
cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'shop_app_shop';")
columns = [row[0] for row in cursor.fetchall()]
print("COLUMNS:", columns)
import psycopg2

conn = psycopg2.connect("postgresql://game_ahopp_ab_user:d03Vl0MfHqEKNiCmXggmDJe7NlbdmIqG@dpg-d9h202naqgkc73dm2n50-a.oregon-postgres.render.com/game_ahopp_ab")
cur = conn.cursor()
cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'shop_app_shop';")
print("COLUMNS:", [row[0] for row in cur.fetchall()])
conn.close()