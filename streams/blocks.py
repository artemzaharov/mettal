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

    english_field = blocks.CharBlock(required=True, help_text='Одно слово на английском или транслитом')
    title = blocks.CharBlock(required=True, help_text='Вид метала')
    text = blocks.RichTextBlock(required=True, help_text='Металл - Цена')

    class Meta:  # noqa
        template = 'streams/metall_block.html'
        icon = "edit"
        label = "Блок цена на металл"

class ReviewsBlock(blocks.StructBlock):

    title = blocks.RichTextBlock(required=True, help_text='Заголовок Отзывы')
    text = blocks.RichTextBlock(required=True, help_text='Текст')
    image1 = ImageChooserBlock(required=False, help_text='Добавить изображение')
    alt1 = blocks.CharBlock(required=False, help_text='Альтернативный текст 1')
    image2 = ImageChooserBlock(required=False, help_text='Добавить изображение')
    alt2 = blocks.CharBlock(required=False, help_text='Альтернативный текст 2')
    image3 = ImageChooserBlock(required=False, help_text='Добавить изображение')
    alt3 = blocks.CharBlock(required=False, help_text='Альтернативный текст 3')

    class Meta:  # noqa
        template = 'streams/reviews_block.html'
        icon = "edit"
        label = "Блок отзывы"
    
class BigTitleBlock(blocks.StructBlock):

    title_thin = blocks.RichTextBlock(required=True, help_text='Заголовок тонкий')
    title_fat = blocks.RichTextBlock(required=True, help_text='Заголовок жирный')

    class Meta:  # noqa
        template = 'streams/big_title_block.html'
        icon = "edit"
        label = "Большой заголовок"


class CallLineBlock(blocks.StructBlock):

    title = blocks.RichTextBlock(required=True, help_text='Заголовок')
    phone = blocks.CharBlock(required=True, help_text='Номер телефона')
    fat_text = blocks.CharBlock(required=True, help_text='Текст жирный')
    thin_text = blocks.CharBlock(required=True, help_text='Текст тонкий')
    

    class Meta:  # noqa
        template = 'streams/call_block.html'
        icon = "edit"
        label = "Блок звонок"

class YandexMapBlock(blocks.StructBlock):

    title = blocks.RichTextBlock(required=False, help_text='Заголовок')

    class Meta:  # noqa
        template = 'streams/yandex_map_block.html'
        icon = "edit"
        label = "Блок карта"

class LineButtonBlock(blocks.StructBlock):

    title = blocks.RichTextBlock(required=True, help_text='Заголовок')
    button_text = blocks.CharBlock(required=True, help_text='Текст кнопки')
    button_url = blocks.URLBlock(required=True, help_text='Ссылка кнопки')
    

    class Meta:  # noqa
        template = 'streams/line_button_block.html'
        icon = "edit"
        label = "Блок линия и кнопка"

class TitleTextBlock(blocks.StructBlock):

    title = blocks.RichTextBlock(required=True, help_text='Заголовок')
    text = blocks.RichTextBlock(required=True, help_text='Текст')
    

    class Meta:  # noqa
        template = 'streams/title_text_block.html'
        icon = "edit"
        label = "Блок заголовок текст"