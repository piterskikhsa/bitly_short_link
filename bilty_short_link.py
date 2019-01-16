import os
import argparse

import requests
from dotenv import load_dotenv


def format_headers(api_token):
    return {'Authorization': 'Bearer {}'.format(api_token) }


def get_split_strip_link(link):
    return link.split('//')[-1].strip('/')


def link_shorten(link, api_token):
    api_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = format_headers(api_token)
    params = {'long_url': link}
    response = requests.post(api_url, headers=headers, json=params)
    if response.ok:
        return response.json()['link']
    raise ValueError('Ссылка указана неверно.')


def link_total_clicks(link, api_token):
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(get_split_strip_link(link))
    response = requests.get(api_url, headers=format_headers(api_token))
    if response.ok:
        return response.json()['total_clicks']
    raise ValueError('Ссылка указана неверно.')


def check_short_link(link, api_token):
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(get_split_strip_link(link))
    response = requests.get(api_url, headers=format_headers(api_token))
    return response.ok


def create_arg_parser():
    parser = argparse.ArgumentParser('Скрипт помогает укоротить ссылку или посмотреть статистику по короткой ссылке.')
    parser.add_argument('url', help='')
    return parser


def main(api_token):
    parser = create_arg_parser()
    namespace = parser.parse_args()

    if check_short_link(namespace.url, api_token):
        response = link_total_clicks(namespace.url, api_token)
    else:
        response = link_shorten(namespace.url, api_token)
    print(response)


if __name__ == '__main__':
    load_dotenv()
    api_token = os.getenv('TOKEN')
    main(api_token)    