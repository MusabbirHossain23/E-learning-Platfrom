from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_chapter_dateof'),
    ]

    operations = [
        migrations.CreateModel(
            name='chapter_content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('dispcription', models.TextField(blank=True)),
                ('chimg', models.ImageField(default=False, upload_to='chaptersimg/')),
                ('chfiles', models.FileField(default=False, upload_to='chfiles/')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.chapter')),
            ],
        ),
    ]
