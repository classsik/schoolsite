# Generated by Django 3.1 on 2020-08-15 17:01

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogindexpage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogindexpage',
            options={'verbose_name': 'Новостная страница'},
        ),
        migrations.AlterModelOptions(
            name='blogpage',
            options={'verbose_name': 'Новость'},
        ),
        migrations.AlterField(
            model_name='blogindexpage',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='Введение'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('Заголовок', wagtail.core.blocks.CharBlock(classname='full title')), ('Параграф', wagtail.core.blocks.RichTextBlock()), ('Изображение', wagtail.images.blocks.ImageChooserBlock())], verbose_name='Тело поста'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(verbose_name='Дата поста'),
        ),
    ]
