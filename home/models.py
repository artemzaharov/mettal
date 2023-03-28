from django.db import models
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet
from streams import blocks
from wagtail.admin.panels import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock



@register_snippet
class Menu(models.Model):
    menu = StreamField([        
        ('menus', blocks.MenuBlock())
    ], use_json_field=True)

    def __str__(self):
        return 'Меню'

    def save(self, *args, **kwargs):
        if Menu.objects.count() >= 1 and not self.pk:
            raise Exception("У вас уже есть меню. Вы не можете создать больше одного")
        super(Menu, self).save(*args, **kwargs)

@register_snippet
class Header(models.Model):
    header = StreamField([        
        ('header', blocks.HeaderBlock())
    ], use_json_field=True)

    def __str__(self):
        return 'Верхушка'
    
    def save(self, *args, **kwargs):
        if Header.objects.count() >= 1 and not self.pk:
            raise Exception("На сайте может быть только одна верхняя часть")
        super(Header, self).save(*args, **kwargs)

@register_snippet
class Footer(models.Model):
    footer = StreamField([        
        ('footer', blocks.FooterBlock())
    ], use_json_field=True)

    def __str__(self):
        return 'Подвал'
    
    def save(self, *args, **kwargs):
        if Footer.objects.count() >= 1 and not self.pk:
            raise Exception("На сайте может быть только одна нижняя часть")
        super(Footer, self).save(*args, **kwargs)

        

class HomePage(Page):
    header = models.ForeignKey(
        'Header', on_delete=models.SET_NULL, null=True, blank=True, related_name='+'
    )
    menu = models.ForeignKey(
        'Menu', on_delete=models.SET_NULL, null=True, blank=True, related_name='+'
    )
    footer = models.ForeignKey(
        'Footer', on_delete=models.SET_NULL, null=True, blank=True, related_name='+'
    )

    

    metall = StreamField([
        ('metall', blocks.MetallBlock())
    ], null=True, blank=True)

    content = StreamField([
        ('review', blocks.ReviewsBlock()),
        ('big_title', blocks.BigTitleBlock()),
        ('call_line', blocks.CallLineBlock()),
        ('yandex_map', blocks.YandexMapBlock()),
        ('line_button', blocks.LineButtonBlock()),
        ('title_text', blocks.TitleTextBlock()),
        ('how_we_buy', blocks.HowWeBuyBlock()),
        
    ])

  
    content_panels = Page.content_panels + [
        FieldPanel("header"),
        FieldPanel("menu"),
        FieldPanel("footer"),
        FieldPanel("metall"),
        FieldPanel("content"),
        
    ]