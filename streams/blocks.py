from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class MenuBlock(blocks.StructBlock):

    title_menu = blocks.CharBlock(required=True, help_text='Название меню')
    title_url = blocks.URLBlock(required=True, help_text='Ссылка на страницу')
    
    class Meta:  # noqa
        template = 'streams/menu_block.html'
        icon = "edit"
        label = "Меню"

class HeaderBlock(blocks.StructBlock):

    logo = ImageChooserBlock(required=False, help_text='Добавить логотип')
    call_us_text = blocks.CharBlock(required=True, help_text='Текст с призывом позвонить')
    call_us_number = blocks.CharBlock(required=True, help_text='Номер телефона')
    email_text = blocks.CharBlock(required=True, help_text='Текст c призывом написать email')
    email_address = blocks.CharBlock(required=True, help_text='Email адрес')
    address_text = blocks.CharBlock(required=True, help_text='Текст с призывом приехать')
    address = blocks.CharBlock(required=True, help_text='Адрес')
    apply_button_text = blocks.CharBlock(required=True, help_text='Кнопка заявки')
    apply_button_url = blocks.URLBlock(required=True, help_text='Ссылка кнопки')

    class Meta:  # noqa
        template = 'streams/header_block.html'
        icon = "edit"
        label = "Верхний блок" 

class FooterBlock(blocks.StructBlock):

    about_us_title = blocks.CharBlock(required=True, help_text='Заголовок о нас')
    about_us_text = blocks.RichTextBlock(required=True, help_text='Текст о нас')
    work_time_title = blocks.CharBlock(required=True, help_text='Заголовок график работы')
    work_time_text = blocks.RichTextBlock(required=True, help_text='Текст график работы')
    services_title = blocks.CharBlock(required=True, help_text='Заголовок услуги')
    services_text = blocks.RichTextBlock(required=True, help_text='Текст услуги')


    class Meta:  # noqa
        template = 'streams/footer_block.html'
        icon = "edit"
        label = "Нижний блок"

class MetallBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text='Заголовок')
    text = blocks.RichTextBlock(required=True, help_text='Текст')

    class Meta:  # noqa
        template = 'streams/metall_block.html'
        icon = "edit"
        label = "Блок цена на металл"