import vk_api
import json

def main():

    # # создаем объект с указанием номера телефона и пароля
    # vk_ses = vk_api.VkApi('littlepeterpony@yahoo.com', 'wFJRyVZn6p')
    
    # # аутентификация
    # try:
    #    vk_ses.auth()
    # except vk_api.AuthError as error_msg:
    #    print(error_msg)
    #    exit(0)
    
    # # объект для выполнения некоторых операций в соц сети
    # vk = vk_ses.get_api()
    
    # # получить json-объект с информацией
    # rs = vk.wall.get(count=0, offset=0)
    # #  сообщения на стене
    # for t in rs['items']:
    #      print(t['text'])
    """ Пример получения всех постов со стены """

    login, password = 'LOGIN', 'PASSWORD'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    tools = vk_api.VkTools(vk_session)

    """ VkTools.get_all позволяет получить все объекты со всех страниц.
        Соответственно get_all используется только если метод принимает
        параметры: count и offset.
        Например может использоваться для получения всех постов стены,
        всех диалогов, всех сообщений, etc.
        При использовании get_all сокращается количество запросов к API
        за счет метода execute в 25 раз.
        Например за раз со стены можно получить 100 * 25 = 2500, где
        100 - максимальное количество постов, которое можно получить за один
        запрос (обычно написано на странице с описанием метода)
    """
    
    # wall = tools.get_all('wall.get', 100, {'owner_id': 1})
    wall = tools.get_all('wall.get', 2, {'owner_id': '-10495776'})

    print('Posts count:', wall['count'])

    if wall['count']:
        print('First post:', wall['items'][0], '\n')
        dictionary = wall['items'][0]
        json_object = json.dumps(dictionary, indent=4, ensure_ascii=False)
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)

    if wall['count'] > 1:
        print('Last post:', wall['items'][-1])

    
if __name__ == '__main__':
    main()