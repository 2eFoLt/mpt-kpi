import requests
import collections
import random


Employee = collections.namedtuple('Employee', 'id first_name last_name surname job_id phone email'.split())

first_names_url = 'https://raw.githubusercontent.com/Raven-SL/ru-pnames-list/refs/heads/master/lists/male_names_rus.txt'
last_names_url = 'https://raw.githubusercontent.com/Raven-SL/ru-pnames-list/refs/heads/master/lists/male_surnames_rus.txt'

first_names = requests.get(first_names_url).content.decode('utf-8').split('\n')
last_names = requests.get(last_names_url).content.decode('utf-8').split('\n')
surnames = [f'{name}ович' for name in first_names]
job_ids = ['Библиотекарь']
phones = ['+7(963)650-42-93']
emails = ['pochta@mail.ru']


def _generate_random_employee(id):
    return Employee(
        id=id,
        first_name=random.choice(first_names),
        last_name=random.choice(last_names),
        surname=random.choice(surnames),
        job_id=random.choice(job_ids),
        phone=random.choice(phones),
        email=random.choice(emails),
    )
employees_list: list[Employee] = [_generate_random_employee(i) for i in range(100)] # Override this to use database requests
