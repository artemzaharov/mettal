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
from .views import sent_telegram
import json

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

    def process_form_submission(self, form):
       
        json_str = json.dumps(form.cleaned_data)
        json_data = json.loads(json_str)
        json_data = json_data.values()
        values_str = ', \n'.join(list(json_data))
        sent_telegram(values_str)
        return self.get_submission_class().objects.create(
            form_data=form.cleaned_data,
            page=self
        )