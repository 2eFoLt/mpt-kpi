import requests
import collections
import random
from flask import url_for
from .criteries_generator import criteries_list


Certificate = collections.namedtuple('Certificate', 'id preview_url criterion_id'.split())

urls = [
    "https://xn----7sbbatcvjrscddclqofaivf1a1pxa.xn--p1ai/images/sertif.jpg",
    "https://www.gostest.com/upload/medialibrary/ff2/ff2d3a6375ca7060f0ce1b5465cfae92.jpg",
    "https://moseac.ru/images/article/5fb68313a9fa6.jpg",
    "https://apit-kovrov.ru/files/uploads/knowledge_base/br1.1-do-2024.jpg",
    "http://127.0.0.1:8000/api/media/test.jpg"
]
# Добавить подгрузку ссылок на документы + превью: <название_дока>, <название_дока>_preview.png
def _generate_random_certificate(id: int, url: str):
    return Certificate(
        id=id,
        preview_url=url,
        criterion_id=random.choice(range(len(criteries_list))),
    )
certificates_list: list[Certificate] = [_generate_random_certificate(i, name) for i, name in enumerate(urls)] # Override this to use database requests
