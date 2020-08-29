from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, RichTextField  # добавляем StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel  # добавляем в StreamField нужные блоки

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class BlogPage(Page):
    date = models.DateField("Дата поста")
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Картинка новости"
    )
    intro = models.CharField(max_length=300, verbose_name="Введение", help_text="Будет показываться в карточке новости", blank=False)
    body = StreamField([
        ('Заголовок', blocks.CharBlock(classname="full title")),
        ('Параграф', blocks.RichTextBlock()),
    ], verbose_name="Тело поста")

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
        ImageChooserPanel('main_image')
    ]

    class Meta:
        verbose_name = "Новость"


class BlogIndexPage(Page):
    intro = RichTextField(blank=True, verbose_name="Введение")

    @property
    def blogs(self):
        # Получить список страниц блога, которые являются потомками этой страницы
        blogs = BlogPage.objects.live().descendant_of(self)

        # Сортировать по дате
        blogs = blogs.order_by('-date')

        return blogs

    def get_context(self, request):
        blogs = self.blogs
        # Пагинация
        page = request.GET.get('page')
        paginator = Paginator(blogs, 9)  # Показывать 9 постов
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        # Обновить контекст шаблона
        context = super(BlogIndexPage, self).get_context(request)
        context['blogs'] = blogs
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    class Meta:
        verbose_name = "Новостная страница"
