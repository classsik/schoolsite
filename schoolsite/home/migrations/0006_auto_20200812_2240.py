# Generated by Django 3.1 on 2020-08-12 17:40

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200812_2232'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='otherpage',
            options={'verbose_name': 'Другие страницы'},
        ),
        migrations.AddField(
            model_name='otherpage',
            name='body',
            field=wagtail.core.fields.StreamField([('Заголовок', wagtail.core.blocks.CharBlock(classname='full title')), ('Параграф', wagtail.core.blocks.RichTextBlock()), ('Изображение', wagtail.images.blocks.ImageChooserBlock())], null=True, verbose_name='Тело страницы'),
        ),
    ]
