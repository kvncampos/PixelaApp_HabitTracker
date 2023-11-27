import requests
import random
import string
import json
from pixela_class import PixelaProfile


# Creates a Custom Token 10 Characters Long
def custom_token():
    """Creates a Custom Token 10 Characters Long"""
    letters = string.ascii_lowercase
    token = ''.join(random.choice(letters) for i in range(10))
    return token


# Creates a Custom Graph ID Unique for User
def custom_graph_id(username):
    "Creates a Custom Graph ID Unique for User"
    letters = string.ascii_lowercase
    token = ''.join(random.choice(letters) for i in range(10))
    custom_id = token + '_' + username
    return custom_id


# Store Credentials of User. This is not best practice as information is saved plain text.
def store_creds(new_user: dict):
    """Checks for file creds_test.py, if found appends new_user if new_user does not exist; otherwise skips.
    if creds_test.py does not exist, it creates the file.
    """
    # Initialize an empty list to store the JSON objects
    stored_data = []

    try:
        # Attempt to read the existing data from the file
        with open('creds_test.py', 'r') as creds_file:
            stored_data = json.load(creds_file)
    except FileNotFoundError:
        # If the file doesn't exist yet, start with an empty list
        print('FileNotFoundError: Will create creds_test.py')

    # Check if the new_user's username is already in the stored data
    username_exists = any(user['username'] == new_user['username'] for user in stored_data)

    if not username_exists:
        # Append the new_user data to the list
        stored_data.append(new_user)

        # Write the updated list of JSON objects back to the file
        with open('creds_test.py', 'w') as creds_file:
            json.dump(stored_data, creds_file, indent=4)
    else:
        print(f"Username '{new_user['username']}' already exists in creds_test.py")


# ------------------------- START OF CODE -------------------------

options_token_question = ['custom', 'create', 'add', '']

# Ask User if they require a Custom Token
choice = input("Do you want a Custom Token or Create Your Own? ").casefold()
while choice not in options_token_question:
    choice = input("Do you want a Custom Token or Create Your Own? ").casefold()

#
if choice == 'custom':
    TOKEN = custom_token()
elif choice in ['create', 'add']:
    TOKEN = input("Type Your Custom or Known Token. [10 Character Min.]").casefold()
    while len(TOKEN) < 10:
        TOKEN = input("Please Use Minumum of 10 Characters. ").casefold()
else:
    TOKEN = None
