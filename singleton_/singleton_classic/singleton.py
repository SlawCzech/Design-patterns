class Singleton:

    _objects = None

    @staticmethod
    def instance():
        if '_instance' not in dir(Singleton):
            Singleton._instance = Singleton()
        return Singleton._instance


s1 = Singleton.instance()
s2 = Singleton.instance()

assert s1 is s2

s1._objects = 42

assert s1._objects == s2._objects

print('assertion passed')

