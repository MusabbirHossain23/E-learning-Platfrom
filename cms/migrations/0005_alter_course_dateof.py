from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_course_dateof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='dateof',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
