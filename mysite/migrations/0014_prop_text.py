# Generated by Django 2.2.1 on 2020-04-07 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_auto_20200404_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prop_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tit', models.CharField(default='title', max_length=200)),
                ('title', models.TextField()),
                ('text', models.TextField()),
                ('img', models.ImageField(default='img', upload_to='img/')),
            ],
        ),
    ]