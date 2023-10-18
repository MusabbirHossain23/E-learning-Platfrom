import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_course_disp'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='dateof',
            field=models.DateField(default=datetime.datetime(2022, 9, 12, 20, 0, 15, 738099)),
        ),
    ]
