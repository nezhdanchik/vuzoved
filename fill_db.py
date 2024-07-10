from django.template.defaultfilters import slugify
from transliterate import translit
import sqlite3
import parse_wiki as pw
from pprint import pprint
from dataclasses import dataclass


def convert_russian_to_slug(s: str):
    return slugify(translit(s, reversed=True))


def get_cursor():
    connection = sqlite3.connect('vusoved/db.sqlite3')
    return connection, connection.cursor()


@dataclass
class University:
    name: str
    description: str
    slug: str = None

    # image = None
    def __post_init__(self):
        self.slug = convert_russian_to_slug(self.name)


def insert_university(university: University):
    connection, cursor = get_cursor()
    cursor.execute(
        f"""
        INSERT INTO vuz_university (name, description, slug)
        VALUES (?,  ?, ?)
        """,
        (university.name, university.description, university.slug)
    )
    connection.commit()
    connection.close()

def add_wiki_url(name, url):
    connection, cursor = get_cursor()
    cursor.execute(
        """
        UPDATE vuz_university
        SET wikipage_url = ? WHERE name = ?
        """,
        (url, name)
    )
    connection.commit()
    connection.close()

# all_universities = pw.get_url_of_moscow_universities()
# for name in all_universities:
#     url = all_universities[name]
#     d = pw.parse_vuz(url)
#     summary = d['summary']
#     university = University(name=name, description=summary)
#     insert_university(university)
#     print(university)

all_universities = pw.get_url_of_moscow_universities()
for name in all_universities:
    url = all_universities[name]
    add_wiki_url(name, url)
    print('DONE',name)
