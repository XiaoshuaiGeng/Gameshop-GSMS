class Game:
    def __init__(self, store_id=None, name='Default Name', release_date='2000-1-1',
                 genre='Unknown', platform='Unknown', price=0.0):
        self.id = store_id
        self.name = name
        self.release_date = release_date
        self.genre = genre
        self.platform = platform
        self.price = price

    # setter / getter
    def set_id(self, store_id):
        self.id = store_id

    def get_id(self):
        return self.id

