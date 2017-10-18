import vk, random
from time import sleep

session = vk.AuthSession('5694610', 'file.destructor@gmail.com', 'deadspringalot16vknew', scope='wall, messages')
vk_api = vk.API(session, v='5.68')

while True:
    
    last_message10 = vk_api.messages.getHistory(count=1, peer_id=2000000010)['items']
    sleep(0.3)
    last_message16 = vk_api.messages.getHistory(count=1, peer_id=2000000016)['items']
    sleep(0.3)
    last_message_target = vk_api.messages.getHistory(count=1, peer_id=1335779)['items']
    sleep(0.3)
    
    if last_message10[0].get('body') == '/check':
        
        users_list = vk_api.messages.getChatUsers(chat_id=10, fields='first_name, last_name, id')
        sleep(0.3)
        rand_user = random.randint(1, len(users_list))
        pidor = users_list[rand_user]['first_name'] + ' ' + users_list[rand_user]['last_name'] + ' является ' \
                                                                                                 'главным ' \
                                                                                                 'пидором ' \
                                                                                                 'прямо ' \
                                                                                                 'сейчас!'
        sleep(0.3)
        user = vk_api.users.get(user_ids=users_list[rand_user]['id'], fields='photo_id')
        sleep(0.3)
        photo = 'photo' + user[0]['photo_id']
        sleep(0.3)
        vk_api.messages.send(chat_id=10, message=str(pidor))
        sleep(0.3)
        vk_api.messages.send(chat_id=10, attachment=photo)
        sleep(0.7)
