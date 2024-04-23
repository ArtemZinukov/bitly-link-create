import requests

TOKEN = "f0374ca8d18153960b27169e34800c556983bd09"  # My token Bitly
url = 'https://api-ssl.bitly.com/v4/shorten'  # Create a short link

info_url = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'  # Info about the short link


def is_bitlink(token, info_url, user_link):  # Info short link or not
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(info_url, headers=headers)
    response.raise_for_status()
    if response.status_code == 200:
        print(f"Ссылка {user_link} является битлинком.")
    else:
        shorten_link(TOKEN, url, user_link)


def shorten_link(token, url, user_link):  # Create the short link
    try:
        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.post(url, headers=headers, json={"long_url": user_link})
        response.raise_for_status()
        print(f"Битлинк {response.json()["link"]}")
        return response.json()["link"]
    except requests.exceptions.HTTPError:
        print("Неверная ссылка")

# try:
#     link = shorten_link(TOKEN, url, user_link)
# except requests.exceptions.HTTPError:
#     print("Неверная ссылка")
# else:
#     print("Успешно!")

# is_bitlink(TOKEN, info_url, user_link)


if __name__ == "__main__":
    user_link = input("Введите ссылку ")
    is_bitlink(TOKEN, info_url, user_link)
    # shorten_link(TOKEN, url, user_link)

