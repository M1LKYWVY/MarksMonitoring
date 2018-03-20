import json
from . import student

try:
    from vedis import Vedis
except ImportError(Vedis):
    print("Please check that vedis was installed through pip3 successfully")
    exit(1)


def __parse_student(dictionary):
    obj = student.Student(dictionary["name"],
                          dictionary["surname"],
                          dictionary["user_name"],
                          dictionary["password"],
                          dictionary["active_semester"],
                          dictionary["tg_chat_id"])
    obj.points = dictionary["points"]
    return obj


def __json_loads(json_object):
    return __parse_student(json.loads(json_object))


def save_user(tg_chat_id, user):
    with Vedis("database.vdb") as db:
        db[tg_chat_id] = json.dumps(user, default=lambda obj: obj.__dict__)


def get_user(tg_chat_id):
    # with Vedis("database.vdb") as db:
    #     return json.loads(db[tg_chat_id], object_hook=lambda obj: namedtuple("Student", obj.keys())(*obj.values()))
    # Down case works fine
    with Vedis("database.vdb") as db:
        return __json_loads(db[tg_chat_id])
    # x = json.dumps(tg_chat_id, default=lambda obj: obj.__dict__)
    # print(x)
    # print(type(__json_loads(x)))
