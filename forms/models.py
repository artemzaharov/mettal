from django.db import models

# Create your models here.
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from home.models import Menu, Header, Footer


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE,
                       related_name='form_fields')


class FormPage(AbstractEmailForm):

    header = models.ForeignKey(
        'home.Header', on_delete=models.SET_NULL, null=True, blank=True, related_name='+'
    )
    menu = models.ForeignKey(
        'home.Menu', on_delete=models.SET_NULL, null=True, blank=True, related_name='+'
    )
    footer = models.ForeignKey(
        'home.Footer', on_delete=models.SET_NULL, null=True, blank=True, related_name='+'
    )

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    template = "forms/form_page.html"
    landing_page_template = "forms/form_landing.html"

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("header"),
        FieldPanel("menu"),
        FieldPanel("footer"),
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]