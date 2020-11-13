class Game:
    def __init__(self, store_id=None, name='Default Name', release_date='2000-1-1',
                 genre=list('Unknown'), platform='Unknown', price=0.0):
        self.id = store_id
        self.name = name
        self.release_date = release_date
        self.genre = genre
        self.platform = platform
        self.price = price

    # setter / getter

    # set_id shouldnt be allowed to use because id is
    # an auto-increament value
    def __set_id__(self, store_id: int):
        self.id = store_id

    def get_id(self):
        return self.id

    def set_name(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name
    
    def set_date(self, date: str):
        self.release_date = date

    def get_date(self) -> str:
        return release_date
    
    def set_genre(self, genre: list) :
        self.genre = genre
    

    def add_genre(self, tag: str):
        self.genre.append(tag)

from DBController import SQLExecutor

cursor = SQLExecutor()
    