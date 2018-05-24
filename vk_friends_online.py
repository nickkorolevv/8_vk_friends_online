import vk
import getpass


APP_ID = "6466857"


def start_session(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends"
    )
    vk_api = vk.API(session, v=version)
    return vk_api


def get_user_login():
    login = input("Введите логин: ")
    return login


def get_user_password():
    password = getpass.getpass("Введите пароль: ")
    return password


def get_online_friends_id():
    friends_id = vk_api.friends.getOnline()
    return friends_id


def get_online_friends(friends_id):
    friends_online = vk_api.users.get(user_ids=friends_id)
    return friends_online


def output_friends_to_console(friends_online, online_now):
    print(online_now)
    for friend_online in friends_online:
        print(friend_online["first_name"], friend_online["last_name"])


if __name__ == "__main__":
    login = get_user_login()
    password = get_user_password()
    version = 5.75
    vk_api = start_session(login, password)
    friends_id = get_online_friends_id()
    friends_online = get_online_friends(friends_id)
    output_friends_to_console(friends_online, "Сейчас онлайн:")
