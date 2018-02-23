from operator import itemgetter

import requests

IMAGE_MAX_WIDTH = 150
members = requests.get('https://www.api.bnk48.com/api/members')

member_images = {
    element['slug'].capitalize(): element['avatar_image']
    for element in members.json()['members']
}

def show_rank(ranks, n=5):
    selected_items = ranks[:n]
    max_size = max(selected_items, key=itemgetter(1))[1]

    def img_tag(name, size):
        image_size = int(size / max_size * IMAGE_MAX_WIDTH)
        return f'''<img src="{member_images[name]}" 
            alt="{name} = {size * 100}%" 
            style="width: {image_size}px; display: inline-block;"/>'''

    return ' '.join([img_tag(*member) for member in ranks[:n]])