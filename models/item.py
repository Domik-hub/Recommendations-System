class Item:
    def __init__(self, data_json):
        self.__id = data_json.get("id")
        self.__genre = data_json.get("genre")

    @property
    def id(self):
        return self.__id

    @property
    def genre(self):
        return self.__genre

    def __str__(self):
        return f"Item ID: {self.__id}, Genre: {self.__genre}"