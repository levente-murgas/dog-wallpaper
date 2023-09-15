import requests
import ctypes
import os
from PIL import Image # pip install pillow, if not installed
import random


def resize_image(image_path, screen_width, screen_height):
    with Image.open(image_path) as img:
        img = img.resize((screen_width, screen_height), Image.ANTIALIAS)
        img.save(image_path)

# Function to set wallpaper and delete image
def set_wallpaper_and_delete(image_path):
    # Set wallpaper to fit the screen
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    # os.remove(image_path)  # Delete the image file

def fetch_image(breed=None):
    if breed:
        url = f"https://dog.ceo/api/breed/{breed}/images/random"
    else:
        url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    data = response.json()
    image_url = data['message']
    image_response = requests.get(image_url)
    return image_response

if __name__ == '__main__':
    # Enter your list of breeds here, for a full list of available breeds, see https://dog.ceo/dog-api/breeds-list
    breeds = ['borzoi', 'australian/shepherd', 'collie/border', 'labrador', 'retriever/golden', 'bullterrier/staffordshire']
    # Choose randomly from breeds
    breed = random.choice(breeds)
    # Fetch image
    image_response = fetch_image(breed)
    # Save the image
    image_path = 'path/to/your/desired/saving/location/for/image.jpg'
    with open(image_path, 'wb') as f:
        f.write(image_response.content)

    screen_width, screen_height = 1920, 1080  # Replace with your screen resolution
    resize_image(image_path, screen_width, screen_height)

    # Set wallpaper and delete image
    set_wallpaper_and_delete(image_path)