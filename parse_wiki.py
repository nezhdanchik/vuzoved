import requests
from bs4 import BeautifulSoup
import re
import pprint

academy = 'https://ru.wikipedia.org/wiki/Академия_акварели_и_изящных_искусств_Сергея_Андрияки'
fin = 'https://ru.wikipedia.org/w/index.php?search=Финансовый%20университет%20при%20Правительстве%20Российской%20Федерации&title=Служебная%3AПоиск&ns0=1'
bauman = 'https://ru.wikipedia.org/wiki/Московский_государственный_технический_университет_имени_Н._Э._Баумана'
urizd = 'https://ru.wikipedia.org/wiki/Всероссийский_государственный_университет_юстиции'


def parse_vuz(url):
    '''
    :param url: url указывающий на страницу вуза
    :return: краткое описание вуза(первый абзац вики), изображение(ещё делается)
    '''
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    block = soup.find('div', attrs={'class': 'mw-content-ltr'})
    # таблица с характеристиками и фото
    # image = block.find('table', attrs={'class': 'infobox'}).img['src']
    texts = block.find_all('p', limit=3)
    summary = None
    for p in texts:
        text = p.text.strip()
        if text.replace(" ", ""):
            # убираем ударения
            text = text.replace('́', '')
            summary = re.sub('\[.*?\]', '', text)
            summary = summary.replace('\xa0', '&nbsp')
            break

    # ВНИМАНИЕ! пока это функционал отключен,так как на многих фото стоит лицензия
    # страница вики, где хранятся изображения разного размера, также там указана лицензия на использование
    # try:
    #     url_page_image = f"https://ru.wikipedia.org{block.find('table', attrs={'class': 'infobox'}).find('a', 'mw-file-description')['href']}"
    # except AttributeError:
    #     url_page_image = None

    return {
        'summary': summary,
        # 'url_page_image': url_page_image
    }


# parse_vuz(bauman)

def parse_page_image(url):
    '''
    :param url: url на страницу с изображением вуза в разных разрешениях
    :return: словарь, где ключ - разрешение изображения, значение - его url
    '''
    if url is None:
        return
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    # блок, где находятся адреса всех изображений с их разрешениями
    block = soup.find('div', attrs={'class': 'mw-filepage-resolutioninfo'})
    images = dict()

    def get_url_and_size_from_a_tag(a_tag):
        image_url = a_tag['href']
        size = str(a_tag.text)
        for i in size:
            if not i.isdigit():
                size = size.replace(i, ' ')
        image_size = tuple(map(int, size.split()))
        return {image_size: image_url}

    # обрабатываем фото по умолчанию
    try:
        images.update(get_url_and_size_from_a_tag(block.a))
        block_other_images = block.find('span', attrs={'class': 'mw-filepage-other-resolutions'})
        other_images = block_other_images.find_all('a')
        for a in other_images:
            images.update(get_url_and_size_from_a_tag(a))
    except TypeError:
        print(f'Ошибка при обработке {url}')
    return images


# print(parse_page_image('https://commons.wikimedia.org/wiki/File:Rsmu_logo.png'))
# pprint.pprint(parse_page_image('https://ru.wikipedia.org/wiki/Файл:Герб_МГТУ_имени_Н._Э._Баумана.svg'))

def get_url_of_moscow_universities():
    '''
    Получаем все вузы москвы
    :return: Словарь, где ключ - название московского университета, значение - его url
    '''
    url = 'https://ru.wikipedia.org/wiki/Категория:Высшие_учебные_заведения_Москвы_по_алфавиту'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    blocks = soup.find_all('div', attrs={'class': 'mw-category-group'})
    urls = dict()
    for block in blocks:
        for li in block.find_all('li'):
            urls[li.a['title']] = f"https://ru.wikipedia.org{li.a['href']}"
    return urls

# pprint.pprint(get_url_of_moscow_universities())
