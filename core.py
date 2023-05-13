import vk_api
from config import acces_token
from vk_api.exceptions import ApiError
from operator import itemgetter

class VkTools():

    def __init__(self, token):
        self.ext_api = vk_api.VkApi(token=token)

    def get_profile_info(self, user_id):
        try:
            info = self.ext_api.method('users.get',
                                       {'user_id': user_id,
                                        'fields': 'bdate,city,sex,first_name,last_name'
                                       }
                                       )[0]
        except ApiError:
            return 'Ошибка get_profile_info'
        print(info)
        return info

    def user_search(self, city_id, age_from, age_to, sex, status=6, offset = None):
        # try:
        profiles = self.ext_api.method('users.search',
                                       {'city_id': city_id,
                                        'age_from': age_from,
                                        'age_to': age_to,
                                        'sex': sex,
                                        'count': 100,
                                        'status': 6,
                                        'offset': offset,
                                        # 'has_photo': 1,

                                       }
                                       )
        # except ApiError:
        #     return 'Ошибка user_search'

        profiles = profiles['items']
        print(profiles)
        print(type(profiles))
        result = []
        for profile in profiles:
            if profile['is_closed'] == False:

                result.append({'name': profile[first_name]  + ' ' + profile[last_name],
                               'id': profile['id']
                               }
                              )
        return result
    # получение 3 топ фото
    def photos_get(self, user_id):
        photos = self.ext_api.method('photos.get',
                                      {'album_id': 'profile',
                                       'owner_id': user_id,
                                       'extended': 1,
                                       'count': 100,

                                      }
                                      )
        try:
            photos = photos['items']
        except KeyError:
            return 'Ошибка photos_get '
        result = []
        # for num, photo in enumerate(photos):
        #     result.append({'owner_id': photo['owner_id'],
        #                    'id': photo['id'],
        #                    'likes': photo['likes'].get('count') + photo['comments'].get('count')
        #                    })
        # result = sorted(result, key=itemgetter('likes'), reverse=True)
        # result = result[0:3]
        for photo in photos:
            # print(photo)
            result.append([photo['likes']['count'], 'photo' + str(photo['owner_id']) + '_' + str(photo['id'])])
        result = sorted(result, reverse=True)[0:3]

        #result = result[0:3]

        # result2 = []
        # result2.append(result)

        return result

#

tools = VkTools(acces_token)
# tools.user_search(36, 1990,1995, 1)
# if __name__ == '__main__':
#     tools = VkTools(acces_token)
# # photos = tools.photos_get(305633358)
#     info = tools.get_profile_info(305633358)
#     print(info)
# bdate_year = info.get('bdate')#.split('.')[2]
# print(bdate_year)
# city_id = info.get('city').get('id')
# print(city_id)
# age_from = int(bdate_year) - 5
# print(age_from)
# age_to = int(bdate_year) + 5
# print(age_to)
# sex = info.get('sex')
# print(sex)
# status = 6
# print(photos)