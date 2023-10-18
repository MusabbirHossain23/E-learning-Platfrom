from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_alter_course_dateof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='cimg',
            field=models.ImageField(default=False, upload_to='courseimg/'),
        ),
    ]
