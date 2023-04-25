class Config:

    def __init__(self, env):
        self.base_url = {
            'local': 'https://localhost/',
            'url': 'https://fakestoreapi.com'
        }[env]
