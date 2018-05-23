import vk
import getpass


APP_ID = "your app_id"


def get_user_login():
    login = input("Введите логин: ")
    return login


def get_user_password():
    password = getpass.getpass("Введите пароль: ")
    return password


def get_user_id(version=5.75):
    user_id = vk_api.users.get(v=version)
    return str(user_id[0]["id"])


def get_online_friends_id(user_id, version=5.75):
    friends_id = vk_api.friends.getOnline(user_id=user_id, v=version)
    return friends_id


def get_online_friends(friends_id, version=5.75):
    friends_online = vk_api.users.get(user_ids=friends_id, v=version)
    return friends_online


def output_friends_to_console(friends_online, online_now):
    print(online_now)
    for friend_online in friends_online:
        print(friend_online["first_name"], friend_online["last_name"])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends"
    )
    vk_api = vk.API(session)
    user_id = get_user_id()
    friends_id = get_online_friends_id(user_id)
    friends_online = get_online_friends(friends_id)
    output_friends_to_console(friends_online, "Сейчас онлайн:")

