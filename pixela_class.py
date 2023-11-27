import requests
import string
import random


class PixelaProfile:
    """Creates a Pixela Object for a UNIQUE Adult User

    """

    def __init__(self, /, username: str, token: str, base_url='https://pixe.la/v1/users'):
        self.username = username
        self.base_url = base_url
        self.original_token = token
        self.initial_params = {
            'token': self.original_token,
            'username': self.username,
            'agreeTermsOfService': 'yes',
            'notMinor': 'yes'
        }

    def __repr__(self):
        return f'Username={self.username!r}, ' \
               f'Token={self.original_token!r}, ' \
               f'PixelaUrl={self.base_url!r}'

    # ------------------------- USER METHODS ----------------------------------------

    def create_pixela_user(self):
        request_output = requests.post(self.base_url, json=self.initial_params)
        return request_output.text

    def update_pixela_user(self):
        update_delete_user_path = f'{self.base_url}/{self.username}'
        put_delete_user_params = {
            'X-USER-TOKEN': self.original_token
        }
        request_output = requests.put(update_delete_user_path, headers=put_delete_user_params)
        return request_output.text

    def delete_pixela_user(self):
        update_delete_user_path = f'{self.base_url}/{self.username}'
        put_delete_user_params = {
            'X-USER-TOKEN': self.original_token
        }
        request_output = requests.delete(update_delete_user_path, headers=put_delete_user_params)
        return request_output.text

    # ------------------------- GRAPH METHODS ----------------------------------------

    def create_graph(self, graph_id: str,
                     name: str,
                     unit: str = 'commit',
                     type: str = 'float',
                     color: str = 'ichou'):  # blue

        create_graph_url = f'{self.base_url}/{self.username}/graphs'
        graph_params = {
            "id": graph_id,
            'name': name,
            'unit': unit,
            'type': type,
            'color': color
        }
        header = {
            'X-USER-TOKEN': self.original_token
        }
        request_output = requests.post(create_graph_url, json=graph_params, headers=header)
        self.store_graph_creds(graph_id, name)
        return request_output.text

    @staticmethod
    def store_graph_creds(graph_id: str, name: str):
        graph_info = {graph_id: name}
        return graph_info

