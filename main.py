import requests
import random
import string
import json
from pixela_class import PixelaProfile


def custom_token():
    letters = string.ascii_lowercase
    token = ''.join(random.choice(letters) for i in range(10))
    return token


def custom_graph_id(username):
    letters = string.ascii_lowercase
    token = ''.join(random.choice(letters) for i in range(10))
    custom_id = token + '_' + username
    return custom_id


def store_creds(new_user: dict):
    # Initialize an empty list to store the JSON objects
    stored_data = []

    try:
        # Attempt to read the existing data from the file
        with open('creds.py', 'r') as creds_file:
            stored_data = json.load(creds_file)
    except FileNotFoundError:
        # If the file doesn't exist yet, start with an empty list
        print('FileNotFoundError: Will create creds.py')

    # Check if the new_user's username is already in the stored data
    username_exists = any(user['username'] == new_user['username'] for user in stored_data)

    if not username_exists:
        # Append the new_user data to the list
        stored_data.append(new_user)

        # Write the updated list of JSON objects back to the file
        with open('creds.py', 'w') as creds_file:
            json.dump(stored_data, creds_file, indent=4)
    else:
        print(f"Username '{new_user['username']}' already exists in creds.py")


choice = input("Do you want a Custom Token or Create Your Own? ").casefold()
if choice == 'custom':
    TOKEN = custom_token()
else:
    TOKEN = choice

joshsimpson = PixelaProfile('joshsimpson', token='rjqrbaxgsp')
joshsimpson_data = vars(joshsimpson)
store_creds(joshsimpson_data)
