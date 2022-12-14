def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance


@singleton
class Database:
    def __init__(self):
        pass


# class Database1(object):
#     pass


d1 = Database()
d2 = Database()
if d1==d2:
    print("yes")
else:
    print("no")