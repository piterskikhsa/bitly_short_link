import os

import requests
from dotenv import load_dotenv


load_dotenv()
api_token = os.getenv('TOKEN')


def format_headers(api_token):
    return {'Authorization': 'Bearer {}'.format(api_token) }


def link_shorten(link, api_token):
    api_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = format_headers(api_token)
    params = {'long_url': link}
    response = requests.post(api_url, headers=headers, json=params)
    if response.ok:
        return response.json()['link']
    raise ValueError('Ссылка указана не верно.')


def link_total_clicks(link, api_token):
    link = link.split('//')[-1].strip('/')
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(link)
    response = requests.get(api_url, headers=format_headers(api_token))
    if response.ok:
        return response.json()['total_clicks']
    raise ValueError('Ссылка указана не верно.')


def check_short_link(link, api_token):
    link = link.split('//')[-1].strip('/')
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(link)
    response = requests.get(api_url, headers=format_headers(api_token))
    return response.ok


def main():
    user_url = input('Введите ссылку: ').strip()
    if check_short_link(user_url, api_token):
        response = link_total_clicks(user_url, api_token)
    else:
        response = link_shorten(user_url, api_token)
    print(response)


if __name__ == '__main__':
    main()    