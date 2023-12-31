import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_alter_course_cimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, max_length=250, null=True, populate_from='cname', unique=True),
        ),
    ]
