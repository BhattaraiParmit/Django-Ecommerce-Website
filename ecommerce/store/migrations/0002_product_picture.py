# Generated by Django 4.0.2 on 2022-02-17 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(default='placeholder.png', upload_to=''),
        ),
    ]