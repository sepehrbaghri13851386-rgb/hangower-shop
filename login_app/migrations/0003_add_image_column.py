from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_profile_dis'),
    ]

    operations = [
        migrations.RunSQL(
            sql='ALTER TABLE login_app_profile ADD COLUMN IF NOT EXISTS image VARCHAR(100);',
            reverse_sql='ALTER TABLE login_app_profile DROP COLUMN IF EXISTS image;',
        ),
    ]