# Generated by Django 4.1.3 on 2023-01-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addcategorydb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('Image', models.ImageField(upload_to='Profile')),
            ],
        ),
    ]
