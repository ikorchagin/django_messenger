# Generated by Django 3.1.2 on 2020-11-02 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='picture',
            field=models.ImageField(null=True, upload_to='chat_pictures', verbose_name='изображение'),
        ),
    ]