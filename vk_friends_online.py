import requests
import json
import time
from misc import TOKEN
from misc import OWNER_ID


def get_friends_id(token, owner_id):
    parameters = {"access_token": token, "owner_id": owner_id, "v": "5.75"}
    id_response = requests.get(
        "https://api.vk.com/method/friends.getOnline",
        params=parameters
    )
    return id_response.json()["response"]


def print_friends_name(friends_id, token):
    for friend_id in friends_id:
        parameters = {
            "v": "5.75",
            "access_token": token,
            "fields": "bdate",
            "user_ids": friend_id
        }
        friends_name = requests.get(
            "https://api.vk.com/method/users.get",
            params=parameters
        )
        print(
            friends_name.json()["response"][0]["first_name"],
            friends_name.json()["response"][0]["last_name"]
        )


if __name__ == "__main__":
    friends_id = get_friends_id(TOKEN, OWNER_ID)
    print_friends_name(friends_id, TOKEN)
