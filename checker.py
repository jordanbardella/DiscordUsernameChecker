import requests
from requests.structures import CaseInsensitiveDict

def check_username(username):
    url = f"https://discord.com/api/v9/unique-username/username-suggestions-unauthed?global_name={username}"
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"

    resp = requests.get(url, headers=headers)
    data = resp.json()

    if data.get("username") == username:
        return True
    else:
        return False

def check(fichier, ctx):
    valide_file = open('valid.txt', 'a')
    invalide_file = open('invalid.txt', 'a')

    try:
        with open(fichier, 'r') as file:
            usernames = file.readlines()

        for username in usernames:
            username = username.strip()
            if check_username(username):
                valide_file.write(username + '\n')
                print("Pseudo Valide : " + username )
            else:
                invalide_file.write(username + '\n')
                print("Pseudo Invalide : " + username )
    finally:
        valide_file.close()
        invalide_file.close()

fichier = 'usernames.txt'
check(fichier)