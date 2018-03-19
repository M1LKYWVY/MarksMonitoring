class User:
    def __init__(self, name, surname, user_name, password, tg_chat_id=54221364):
        self.name = name
        self.surname = surname
        self.user_name = user_name
        self.password = password
        self.tg_chat_id = tg_chat_id
        self.semester = [{}]
