import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from datetime import datetime
from config import acces_token
from core import tools
from operator import itemgetter
from config import acces_token, community_token
import base
from random import randrange

class BotInterface:

    def __init__(self, token):
        self.bot = vk_api.VkApi(token=token)

    def message_send(self, user_id, message=None, attachment=None):
        self.bot.method('messages.send',
                  {'user_id': user_id,
                   'message': message,
                   'attachment': attachment,
                   'random_id': randrange(100)
                   }
                  )

    def handler(self):
        # global city_id
        offset = 0
        longpull = VkLongPoll(self.bot)
        for event in longpull.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                info=tools.get_profile_info(event.user_id)
                print(info)
                bdate_year = info.get('bdate').split('.')[2]
                print(bdate_year)
                if bdate_year is None:
                    self.message_send(event.user_id, 'Укажите год рождения')
                city_id = info.get('city').get('id')
                print(city_id)
                print(type(city_id))
                if city_id is None:
                    self.message_send(event.user_id, 'Укажите город в вашем профиле')
                age = age_from = int(bdate_year) - 5
                age_to = int(bdate_year) + 5
                status = 6
                sex = info.get('sex')

                if event.text.lower() == 'привет':
                    self.message_send(event.user_id, 'Привет, напиши поиск, чтобы найти пару!')

                elif event.text.lower() == 'поиск' and sex == 1:
                    if event.text.lower() == 'поиск' and sex == 1:
                        sex = 2
                        self.message_send(event.user_id, 'Начинаем искать вам мужчину!')
                    elif event.text.lower() == 'поиск' and sex == 2:
                        sex = 1
                        self.message_send(event.user_id, 'Начинаем искать вам женщину!')
                    else:
                        self.message_send(event.user_id, 'Введите ваш пол: 1(женщина), 2(мужчина)')
                        if event.text.lower() == '1':
                            sex = 2
                        if event.text.lower() == '2':
                            sex = 1

                        self.message_send(event.user_id, 'Ищем партнера в вашем городе?')
                        if event.text.lower() == 'да':
                            continue
                        else:
                            self.message_send(event.user_id, 'Укажите город')
                            if len(event.text.lower()) > 1:
                                city_id = event.text.lower()
                    print(type(city_id))
                    list_profiles_for = tools.user_search(self, city_id, age_from, age_to, sex, status)
                    print(list_profiles_for)
                    list_profiles = create_db(conn, event.user_id)
                    for l_profile in list_profiles_for:
                        # offset += 1
                        user_id = l_profile.get('id')
                        first_name = l_profile.get('first_name')
                        last_name = l_profile.get('last_name')
                        name_profiles = first_name + last_name
                        # search_foto =  photos_get(self, user_id)

                        print(l_profile)
                        list_id_profile = []
                        for list_is in list_id_profile:
                            list_id_profile.append(x[0])
                        if search_id in list_id_profile:
                            continue
                        else:
                            insert_profiles(conn, event.id_user, search_id)
                            self.message_send(event.user_id, 'https://vk.com/id' + str(search_id))
                            new_list_fhotos = photos_get(search_id)
                            for new_photo in new_list_fhotos:
                                photo_id = new_photo.get('id')
                                owner_id = new_photo.get('owner_id')
                                media = 'photo' + str(owner_id) + '_' + str(photo_id)
                                self.message_send(event.user_id, attachment=media)
                    self.message_send(event.user_id, 'Напишите "поиск" или "далее", если хотите продолжить поиск!')
                else:
                    self.message_send(event.user_id, 'Ошибка. Напиши привет')
                print(event.user_id, bdate_year, sex)

        # def start_bot(self):
        #     response = 'Добро пожаловать в бот Vkinder.\n Напиши привет, чтобы начать!'
        #     return response

if __name__ == '__main__':
    bot = BotInterface(community_token)
    bot.handler()
    media = 'photo709972942_457239017'
    # bot.message_send(305633358, 'фото', attachment=media)
    # (bot.handler(user_id, 'фото', attachment=media))


# if len(event.text.lower()) > 1:
                #         city_id = event.text.lower()