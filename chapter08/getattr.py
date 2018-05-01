# __getattr__, __getattribute__
# __getattr__ 就是在查找不到属性的时候调用


class User:
    def __init__(self, info={}):
        self.info = info

    def __getattr__(self, item):
        return "bobby1"

    def __getattribute__(self, item):
        return "bobby2"


if __name__ == "__main__":
    user = User(info={})
    print(user.nam)
