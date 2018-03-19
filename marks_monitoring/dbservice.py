try:
    from vedis import Vedis
except ImportError:
    print("Please check that vedis was installed through pip3 successfully")
    exit(1)


def save_user(tg_chat_id, user):
    with Vedis("database.vdb") as db:
        db[tg_chat_id] = user
    # TODO get json from object


def get_user(tg_chat_id):
    with Vedis("database.vdb") as db:
        return db[tg_chat_id]
    # TODO get object from json
