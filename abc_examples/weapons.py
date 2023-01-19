import abc


class SwordMeta(type):
    def __subclasscheck__(cls, subclass):
        if (
                hasattr(subclass, 'swipe') and callable(subclass.swipe)
                and
                hasattr(subclass, 'sharpen') and callable(subclass.sharpen)
        ):
            return True
        return super().__subclasscheck__(subclass)

    def __instancecheck__(cls, instance):
        return (
            issubclass(type(instance), cls)
        )


class Sword(abc.ABC):
    # @classmethod
    # def __subclasshook__(cls, subclass):
    #     return (hasattr(subclass, 'swipe') and callable(subclass.swipe)
    #             and
    #             hasattr(subclass, 'sharpen') and callable(subclass.sharpen)
    #             ) or NotImplemented

    @abc.abstractmethod
    def swipe(self):
        raise NotImplementedError

    @abc.abstractmethod
    def sharpen(self):
        raise NotImplementedError

    def thrust(self):
        print('Thrust!', type(self).__name__)


class BroadSword(Sword):
    def swipe(self):
        print('Swoosh!', type(self).__name__)

    def sharpen(self):
        print('Shink', type(self).__name__)


class SamuraiSword(Sword):
    def swipe(self):
        print('Slice!', type(self).__name__)

    def sharpen(self):
        print('Shink', type(self).__name__)


class Rifle:
    def fire(self):
        print('Bang!', type(self).__name__)


# class Sabre(Sword):
#     pass


# @Sword.register
class LightSabre:
    def swipe(self):
        print('wzoom', type(self).__name__)

#
# print(Sword.swipe.__isabstractmethod__)
# print(BroadSword.swipe.__isabstractmethod__)
# print(getattr(Sword.thrust, '__isabstractmethod__', None))
# print(issubclass(LightSabre, Sword))
# print(issubclass(BroadSword, Sword))
# print(BroadSword.__mro__)
# print(issubclass(SamuraiSword, Sword))
# print(issubclass(Rifle, Sword))
#
# ss = SamuraiSword()
#
# print(isinstance(ss, Sword))

#
# print(issubclass(Sabre, Sword))
# print(Sabre.__mro__)

#
# bs = BroadSword()
# print(isinstance(bs, Sword))
# bs.swipe()
# # bs.thrust()
#
# print(BroadSword.__mro__)


# class Text(metaclass=abc.ABCMeta):
#     pass
#
#
# Text.register(str)
#
# print(issubclass(str, Text))
# print(isinstance('dupa', Text))
#
#
# @Text.register
# class SimpleText:
#     pass
#
# print(issubclass(SimpleText, Text))
#
# from numbers import Real
#
# print(issubclass(float, Real))
# print(float.__mro__)