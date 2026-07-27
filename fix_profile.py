import psycopg2
import time

url = "postgresql://game_ahopp_ab_user:d03Vl0MfHqEKNiCmXggmDJe7NlbdmIqG@dpg-d9h202naqgkc73dm2n50-a.oregon-postgres.render.com/game_ahopp_ab"

for attempt in range(5):
    try:
        conn = psycopg2.connect(url, connect_timeout=15)
        cur = conn.cursor()
        cur.execute("ALTER TABLE login_app_profile RENAME COLUMN avatar TO image;")
        conn.commit()
        cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'login_app_profile';")
        print("COLUMNS:", [row[0] for row in cur.fetchall()])
        conn.close()
        break
    except Exception as e:
        print(f"Attempt {attempt+1} failed: {e}")
        time.sleep(3)