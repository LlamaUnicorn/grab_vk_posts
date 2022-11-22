import os
import requests
import json


my_secret = os.environ['TOKEN']

NUMBER_OF_POSTS_TO_GET = 1

# Disabled to prevent reaching API-calls limit
# Uncomment when it's finished

get_response = requests.get(f'https://api.vk.com/method/wall.get?domain=vokki_group&count={NUMBER_OF_POSTS_TO_GET}&filter=owner&access_token={my_secret}&v=5.131')
post_text = get_response.json()['response']['items'][0]['text']
print(post_text)
# Save text

with open("response.txt", "w") as file:
    # response = get_response.text
    # print(type(response))
    file.writelines(post_text)
    # file.writelines(get_response.text)
    # file.write(get_response.text)


# Save JSON

# with open('data.json', 'w') as file:
#     # data = json.load(file)
#     # print(data['response']['items'][0]['text'])
#     # data2 = data['response']['items'][0]['text']
#     json_string = json.dumps(post_text, indent=2, ensure_ascii=False)
#     print(json_string)

# print(x)
# x.json()




# def write_json(data):
#     with open('data.json', 'w') as file:
#         json.dump(data, file, indent=2, ensure_ascii=False)

# write_json(x.json())




  
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