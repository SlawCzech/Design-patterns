from importlib import import_module
from inspect import getmembers, isclass, isabstract

from factory.full_factory.factories.abs_factory import AbsFactory


def load_factory(factory_name):
    try:
        factory_module = import_module('.' + factory_name, 'factories')
    except ImportError:
        factory_module = import_module('.null_factory', 'factories')

    classes = getmembers(factory_module, lambda x: isclass(x) and not isabstract(x))

    for _, class_ in classes:
        if issubclass(class_, AbsFactory):
            return class_()
