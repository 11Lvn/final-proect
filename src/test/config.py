import configparser
import os

import yaml


def get_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'config.yaml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def get_offers_config():
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'offers.ini')
    config.read(config_path, encoding='UTF-8')

    offers = []
    for key in config['OFFERS']:
        if key.startswith('title'):
            index = key.split('_')[-1] if '_' in key else ''
            offer = {
                'title': config['OFFERS'][key],
                'type': config['OFFERS'].get(f'TYPE_{index}', None),
                'audience': config['OFFERS'].get(f'AUDIENCE_{index}', None),
                'publish_date': config['OFFERS'].get(f'PUBLISH_DATE_{index}', None),
                'cancel_date': config['OFFERS'].get(f'CANCEL_DATE_{index}', None),
                'offer': config['OFFERS'].get(f'OFFER_{index}', None),
                'text': config['OFFERS'].get(f'TEXT_{index}', None),
                'image': config['OFFERS'].get(f'IMAGE_{index}', None),
                'show_for_student': config['OFFERS'].getboolean(f'SHOW_FOR_STUDENT_{index}', False)
            }
            offers.append(offer)

    return offers
