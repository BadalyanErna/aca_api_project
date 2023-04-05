# class Config:
#     def __init__(self, env):
#         self.base_url = {
#             'local': 'https://localhost/',
#         }[env]
#
#

class Config:

    def __init__(self, env):
        self.base_url = {
            'local': 'https://localhost/',
            'url': 'https://fakestoreapi.com'
        }[env]

        self.user_login = {
            'username': "mor_2314",
            'password': "83r5^_"
        }