# Generated by Django 3.0 on 2020-01-05 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://images.app.goo.gl/eUfxDEeTQte98ZFB8', max_length=500),
        ),
    ]
