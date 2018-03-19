import json
from collections import namedtuple

try:
    from vedis import Vedis
except ImportError:
    print("Please check that vedis was installed through pip3 successfully")
    exit(1)


def save_user(tg_chat_id, user):
    with Vedis("database.vdb") as db:
        db[tg_chat_id] = json.dumps(user, default=lambda y: y.__dict__)


def get_user(tg_chat_id):
    with Vedis("database.vdb") as db:
        return json.loads(db[tg_chat_id], object_hook=lambda d: namedtuple("Student", d.keys())(*d.values()))
