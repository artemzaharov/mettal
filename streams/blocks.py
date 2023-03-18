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