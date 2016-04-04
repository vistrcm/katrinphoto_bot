import requests
import random


def get_items():
    r = requests.get("http://lene.pois.org.ru/Katrin/items")
    return [_["img"] for _ in r.json()]


def get_sorted_items():
    return sorted(get_items())


def get_latest():
    return get_sorted_items()[-1]


def get_random():
    return random.choice(get_items())