class User:
    def __init__(self, data_json):
        self.__id = data_json.get("user_id")
        self.__liked_items = data_json.get("liked_items", [])

    @property
    def id(self):
        return self.__id

    @property
    def liked_items(self):
        return self.__liked_items

    def __str__(self):
        return f"User ID: {self.__id}, Liked Items: {self.__liked_items}"