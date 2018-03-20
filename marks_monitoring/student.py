class Student(object):
    def __init__(self, name, surname, user_name, password, active_semester=1, tg_chat_id=54221364):
        self.name = name
        self.surname = surname
        self.user_name = user_name
        self.password = password
        self.tg_chat_id = tg_chat_id
        self.active_semester = active_semester
        self.points = [{}]
