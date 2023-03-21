from django.db import models
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet
from streams import blocks
from wagtail.admin.panels import FieldPanel


@register_snippet
class Menu(models.Model):
    menu = StreamField([        
        ('menus', blocks.MenuBlock())
    ], use_json_field=True)

    def __str__(self):
        return 'Меню'


@register_snippet
class Header(models.Model):
    header = StreamField([        
        ('header', blocks.HeaderBlock())
    ], use_json_field=True)

    def __str__(self):
        return 'Верхушка'

@register_snippet
class Footer(models.Model):
    footer = StreamField([        
        ('footer', blocks.FooterBlock())
    ], use_json_field=True)

    def __str__(self):
        return 'Подвал'

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


    content_panels = Page.content_panels + [
        FieldPanel("header"),
        FieldPanel("menu"),
        FieldPanel("footer"),
        FieldPanel("metall"),
    ]