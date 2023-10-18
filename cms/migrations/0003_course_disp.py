from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_alter_teacher_email_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='disp',
            field=models.TextField(default=False),
        ),
    ]
