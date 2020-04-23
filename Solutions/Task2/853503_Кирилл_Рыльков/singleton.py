class Singleton(type):
    instances ={}
    def __call__(cls, *args, **kwargs):
        if(cls not in cls.instances):
            cls.instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instances[cls]

class Demo(metaclass=Singleton):
    state ="On"


if __name__ == '__main__':
    demo1 = Demo()
    demo2 = Demo()

    print(demo1)
    print(demo2)
