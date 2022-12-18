import os
import requests
import json
from datetime import datetime

# Set the number of posts to get and the offset (if applicable)
NUMBER_OF_POSTS_TO_GET = 1
OFFSET = 3

# Get the access token from the environment variable
ACCESS_TOKEN = os.environ['TOKEN']

def get_post_text(response_json):
    """Extract the text of the first post from the response JSON."""
    return response_json['response']['items'][0]['text']

def save_post_text(text, file_name):
    """Save the post text to a file."""
    with open(file_name, "w") as file:
        file.write(text)

def save_json(json_data, file_name):
    """Save the JSON data to a file."""
    with open(file_name, "w") as file:
        json.dump(json_data, file, indent=2, ensure_ascii=False)

def download_image(image_url):
    """Download an image from the given URL."""
    response = requests.get(image_url)
    return response.content

def save_image(image_data, file_name):
    """Save image data to a file."""
    with open(file_name, "wb") as file:
        file.write(image_data)

def get_largest_resolution_image_url(sizes):
    """Get the URL of the largest resolution image in the given list of sizes."""
    for letter in reversed("abcdefghijklmnopqrstuvwxyz"):
        image_url = next((item['url'] for item in sizes if item["type"] == letter), None)
        if image_url:
            return image_url
    return None

def create_folder(folder_name):
    """Create a folder with the given name if it does not exist."""
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def download_images(image_urls, folder_name):
    """Download images from the given URLs and save them to the specified folder."""
    for i, image_url in enumerate(image_urls):
        # Download the image
        image_data = download_image(image_url)

        # Save the image to a file
        image_file_name = f"{str(i+1).zfill(2)}.png"
        save_image(image_data, os.path.join(folder_name, image_file_name))

def download_text_files(text_files, folder_name):
    """Download text files from the given URLs and save them to the specified folder."""
    for i, text_file in enumerate(text_files):
        # Download the text file
        text_file_data = download_text_file(text_file)

        # Save the text file to a file
        text_file_name = f"{str(i+1).zfill(2)}.txt"
        save_text_file(text_file_data, os.path.join(folder_name, text_file_name))

def download_text_file(text_file_url):
    """Download a text file from the given URL."""
    response = requests.get(text_file_url)
    return response.content

def save_text_file(text_file_data, file_name):
    """Save text file data to a file."""
    with open(file_name, "w") as file:
        file.write(text_file_data)

def download_json_files(json_files, folder_name):
    """Download JSON files from the given URLs and save them to the specified folder."""
    for i, json_file in enumerate(json_files):
        # Download the JSON file
        json_file_data = download_json_file(json_file)

        # Save the JSON file to a file
        json_file_name = f"{str(i+1).zfill(2)}.json"
        save_json_file(json_file_data, os.path.join(folder_name, json_file_name))

def download_json_file(json_file_url):
    """Download a JSON file from the given URL."""
    response = requests.get(json_file_url)
    return response.json()

def save_json_file(json_file_data, file_name):
    """Save JSON file data to a file."""
    with open(file_name, "w") as file:
        json.dump(json_file_data, file, indent=2, ensure_ascii=False)

# Make the request to the VK API
response = requests.get(f'https://api.vk.com/method/wall.get?domain=vokki_group&count={NUMBER_OF_POSTS_TO_GET}&offset={OFFSET}&filter=owner&access_token={ACCESS_TOKEN}&v=5.131')

# Get the text of the first post
post_text = get_post_text(response.json())

# Save the post text to a file
save_post_text(post_text, "response.txt")

# Save the JSON data to a file
save_json(response.json(), "data2.json")

# Check if the post has any attachments
attachments = response.json()['response']['items'][0]['attachments']
if attachments:
    # Get the current date and time
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d_%H-%M")

    # Create a folder with the current date and time
    folder_name = f"{date_time}"
    create_folder(folder_name)

    # Get the URLs of all the images, text files, and JSON files in the post
    image_urls = []
    text_file_urls = []
    json_file_urls = []
    for attachment in attachments:
        if attachment['type'] == "photo":
            sizes = attachment['photo']['sizes']
            image_url = get_largest_resolution_image_url(sizes)
            if image_url:
                image_urls.append(image_url)
        elif attachment['type'] == "text":
            text_file_urls.append(attachment['text']['url'])
        elif attachment['type'] == "json":
            json_file_urls.append(attachment['json']['url'])

    # Download and save the images
    if image_urls:
        download_images(image_urls, folder_name)

    # Download and save the text files
    if text_file_urls:
        download_text_files(text_file_urls, folder_name)

    # Download and save the JSON files
    if json_file_urls:
        download_json_files(json_file_urls, folder_name)
