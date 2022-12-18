import os
import requests
import json


my_secret = os.environ['TOKEN']
NUMBER_OF_POSTS_TO_GET = 1
OFFSET = 1

# Disabled to prevent reaching API-calls limit
# Uncomment when it's finished

get_response = requests.get(f'https://api.vk.com/method/wall.get?domain=vokki_group&count={NUMBER_OF_POSTS_TO_GET}&offset={OFFSET}&filter=owner&access_token={my_secret}&v=5.131')
post_text = get_response.json()['response']['items'][0]['text']

# print(post_text)


# Save post text to a text file

with open("response.txt", "w") as file:
    # response = get_response.text
    # print(type(response))
    file.writelines(post_text)
    # file.writelines(get_response.text)
    # file.write(get_response.text)


# Save JSON

data = get_response.json()
with open('data2.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    # post_text = data['response']['items'][0]['text']



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
    # print(json_data)

print(data['response']['items'][0]['attachments'][0]['photo']['sizes'])
sizes = data['response']['items'][0]['attachments'][0]['photo']['sizes']
print('-'*10)
print(sizes)
print(type(sizes))

# Get url of the biggest resolution image
final_url_dict = next((item for item in sizes if item["type"] == "z"), None)
print(final_url_dict)
final_url = final_url_dict['url']
print(final_url)
# Get index
# next((i for i, item in enumerate(sizes) if item["type"] == "x"), None)
# if 'type'
# worked for albums, didn't for photos

# print(data['response']['items'][0]['copy_history'][0]['attachments'][0])

# Download image
response3 = requests.get(final_url)

with open("sample_image3.png", "wb") as file:
    file.write(response3.content)


# # Opening JSON file
# f = open('data.json')
  
# # returns JSON object as 
# # a dictionary
# data = json.load(f)
  
# # Iterating through the json
# # list
# for i in data['emp_details']:
#     print(i)
  
# # Closing file
# f.close()




# def main():
#     group_id = '-10495776'
#     r = requests.get('https://api.vk.com/method/wall.get', params={'owner_id': group_id, 'count':5, 'offset': 0})
#     write_json(r.json())


# if __name__ == '__main__':
#     main()