from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import StreamFieldPanel, InlinePanel, FieldPanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from modelcluster.fields import ParentalKey


#TODO: сделать баннер
#TODO: начать галерею



class HomePage(Page):
    carousel_image_one = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Изображение для карусели 1"
    )

    carousel_image_two = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Изображение для карусели 2"
    )
    content_panels = Page.content_panels + [
        ImageChooserPanel("carousel_image_one"),
        ImageChooserPanel("carousel_image_two")
    ]


class UrlPage(Page):
    body = StreamField([
        ('Заголовок', blocks.CharBlock(classname="full title")),
        ('Страница', blocks.PageChooserBlock(required=False)),

    ], verbose_name="Тело страницы")

    content_panels = Page.content_panels + [
        StreamFieldPanel("body")
    ]

    class Meta:
        verbose_name = "Страница с ссылками"


class OtherPage(Page):
    body = StreamField([
        ('Заголовок', blocks.CharBlock(classname="full title")),
        ('Параграф', blocks.RichTextBlock()),
        ('Изображение', ImageChooserBlock()),
    ], verbose_name="Тело страницы", null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Другие страницы"


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='custom_form_fields')


class FormPage(AbstractEmailForm):
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        InlinePanel('custom_form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email Notification Config"),
    ]

    def get_form_fields(self):
        return self.custom_form_fields.all()