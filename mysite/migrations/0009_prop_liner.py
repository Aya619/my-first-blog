# Generated by Django 2.2.1 on 2020-03-09 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_auto_20200227_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prop_liner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('sub', models.CharField(blank=True, max_length=200)),
                ('text', models.TextField()),
                ('img', models.ImageField(default='img', upload_to='img/')),
            ],
        ),
    ]
