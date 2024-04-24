import requests
import os
from dotenv import load_dotenv, find_dotenv

url = 'https://api-ssl.bitly.com/v4/shorten'  # Create a short link

info_url = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'  # Info about the short link

load_dotenv(find_dotenv())


def is_bitlink(token, info_url, user_link):  # Info short link or not
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(info_url, headers=headers)
    response.raise_for_status()
    if response.status_code == 200:
        return f"Ссылка {user_link} является битлинком."
    # else:
        # shorten_link(TOKEN, url, user_link)


def shorten_link(token, url, user_link):  # Create the short link
    try:
        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.post(url, headers=headers, json={"long_url": user_link})
        response.raise_for_status()
        link_output = f"Битлинк {response.json()["link"]}"
        return link_output
    except requests.exceptions.HTTPError:
        return "Неверная ссылка"


def main():
    print(shorten_link(token, url, user_link))  # Вот тут хотел написать is_bitlink, а в нем else запускает shorten_link


if __name__ == "__main__":
    user_link = input("Введите ссылку ")
    token = os.getenv('TOKEN')
    main()

