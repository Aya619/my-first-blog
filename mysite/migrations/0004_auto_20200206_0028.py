# Generated by Django 2.2.1 on 2020-02-05 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_lin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prop_cal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('img', models.ImageField(default='img', upload_to='img/')),
            ],
        ),
        migrations.DeleteModel(
            name='Lin',
        ),
    ]
