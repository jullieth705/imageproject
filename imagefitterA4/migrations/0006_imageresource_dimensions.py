# Generated by Django 4.0.2 on 2022-02-15 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagefitterA4', '0005_alter_imageresource_orientation'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageresource',
            name='dimensions',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]