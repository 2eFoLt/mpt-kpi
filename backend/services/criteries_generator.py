import requests
import collections
import random


Criterion = collections.namedtuple('Criterion', 'id name mark_from mark_to'.split())

urls = [
    "Привлечение дополнительных средств и спонсорской помощи для развития библиотеки",
    "Публикации и освещение опыта методической работы библиотек в средствах массовой информации",
    "Oрганизация и участие в мероприятиях муниципального и регионального уровня",
    "Участие в разработке локальных нормативных документов",
]


def _generate_random_criterion(id: int, name: str):
    return Criterion(
        id=id,
        name=name,
        mark_from=random.choice(range(0, 10)),
        mark_to=random.choice(range(10, 20)),
    )
criteries_list: list[Criterion] = [_generate_random_criterion(i, name) for i, name in enumerate(urls)] # Override this to use database requests
