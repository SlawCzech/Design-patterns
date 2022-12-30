import abc


class MyAbc(abc.ABC):
    @abc.abstractmethod
    def do_something(self, value):
        pass

    @property
    @abc.abstractmethod
    def some_property(self):
        pass


class MyClass(MyAbc):
    @property
    def some_property(self):
        return None

    def do_something(self, value):
        pass


n = MyClass()
