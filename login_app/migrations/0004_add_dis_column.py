from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_add_image_column'),
    ]

    operations = [
        migrations.RunSQL(
            sql="ALTER TABLE login_app_profile ADD COLUMN IF NOT EXISTS dis TEXT NOT NULL DEFAULT '1';",
            reverse_sql="ALTER TABLE login_app_profile DROP COLUMN IF EXISTS dis;",
        ),
    ]