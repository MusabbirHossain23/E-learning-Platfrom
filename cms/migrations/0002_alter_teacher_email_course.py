from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=250, unique=True),
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=400)),
                ('slug', models.SlugField()),
                ('cimg', models.ImageField(upload_to='courseimg/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.teacher')),
            ],
        ),
    ]
