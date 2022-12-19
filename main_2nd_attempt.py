import os
import requests
import json
import datetime

# Create a folder with current date and time
now = datetime.datetime.now()
folder_name = now.strftime("%Y-%m-%d_%H-%M")
os.makedirs(folder_name)

my_secret = os.environ['TOKEN']
NUMBER_OF_POSTS_TO_GET = 1
OFFSET = 1

# Disabled to prevent reaching API-calls limit
# Uncomment when it's finished

get_response = requests.get(f'https://api.vk.com/method/wall.get?domain=vokki_group&count={NUMBER_OF_POSTS_TO_GET}&offset={OFFSET}&filter=owner&access_token={my_secret}&v=5.131')
post_text = get_response.json()['response']['items'][0]['text']

# Save post text to a text file

with open(f"{folder_name}/response.txt", "w") as file:
    file.writelines(post_text)

# Save JSON

data = get_response.json()
with open(f"{folder_name}/data2.json", 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Save image

# Look for an image URL

# Check if photo or album exists in JSON

JSON_check = 'data2.json'
with open(JSON_check, 'r') as f:
    if "photo" in JSON_check:
        print('photo exists')
    else:
        print('photo doesn\'t exist')
    json_data = json.load(f)

sizes = data['response']['items'][0]['attachments'][0]['photo']['sizes']

# Get url of the biggest resolution image
final_url_dict = next((item for item in sizes if item["type"] == "z"), None)
final_url = final_url_dict['url']

# Download image
response3 = requests.get(final_url)

with open(f"{folder_name}/sample_image3.png", "wb") as file:
    file.write(response3.content)
