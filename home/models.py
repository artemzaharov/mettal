from django.db import models
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet
from streams import blocks
from wagtail.admin.edit_handlers import FieldPanel



@register_snippet
class Menu(models.Model):
    ''' Alows to translate menus '''
    menu = StreamField([        
        ('menus', blocks.MenuBlock())
    ])

    def __str__(self):
        return 'Menu'


class HomePage(Page):
    menu = models.ForeignKey(
        'Menu', on_delete=models.SET_NULL, null=True, blank=True, related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel("menu"),
    ]