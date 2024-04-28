import requests
import os
from dotenv import load_dotenv, find_dotenv
from urllib.parse import urlparse


def count_click(token, netloc, path):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{netloc}/{path}/clicks/summary'
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "unit": "day",
        "units": -1
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    clicks_count = response.json()['total_clicks']
    return clicks_count


def shorten_link(token, user_link):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(url, headers=headers, json={"long_url": user_link})
    response.raise_for_status()
    link_output = response.json()['link']
    return link_output


def is_bitlink(token, netloc, path):
    info_url = f'https://api-ssl.bitly.com/v4/bitlinks/{netloc}/{path}'
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(info_url, headers=headers)
    if not response.ok:
        return
    return True


def main():
    load_dotenv(find_dotenv())
    user_link = input("Введите ссылку ")
    token = os.environ['BITLY_TOKEN']
    url_parsing = urlparse(user_link)
    netloc = url_parsing.netloc
    path = url_parsing.path
    try:
        bitlink = is_bitlink(token, netloc, path)
        if bitlink:
            transition_count = count_click(token, netloc, path)
            print(f"Количество переходов по ссылке: {transition_count}")
        else:
            shot_link = shorten_link(token, user_link)
            print(f"Ваш битлинк: {shot_link}")
    except requests.exceptions.HTTPError:
        print("Неверная ссылка")


if __name__ == "__main__":
    main()
