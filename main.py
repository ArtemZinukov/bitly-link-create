import requests
import os
from dotenv import load_dotenv, find_dotenv
from urllib.parse import urlparse


def is_bitlink(token, user_link):  # Info short link or not
    parsed = urlparse(user_link)
    netloc = parsed.netloc
    path = parsed.path
    INFO_URL = f'https://api-ssl.bitly.com/v4/bitlinks/{netloc}/{path}'
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(INFO_URL, headers=headers)
    response.raise_for_status()
    if response.ok:
        count_click(token, netloc, path)
    else:
        shorten_link(token, user_link)


def count_click(token, netloc, path):  # Count click for link
    URL = f'https://api-ssl.bitly.com/v4/bitlinks/{netloc}/{path}/clicks/summary'
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "unit": "day",
        "units": -1
    }
    response = requests.get(URL, headers=headers, params=params)
    response.raise_for_status()
    clicks_count = f"Количество кликов по ссылке: {response.json()["total_clicks"]}"
    return clicks_count


def shorten_link(token, user_link):  # Create the short link
    URL = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(URL, headers=headers, json={"long_url": user_link})
    response.raise_for_status()
    link_output = f"Битлинк {response.json()["link"]}"
    return link_output


def main():
    load_dotenv(find_dotenv())
    user_link = input("Введите ссылку ")
    token = os.environ['TOKEN_BITLY']
    try:
        print(is_bitlink(token, user_link))
    except requests.exceptions.HTTPError:
        print("Неверная ссылка")


if __name__ == "__main__":
    main()
