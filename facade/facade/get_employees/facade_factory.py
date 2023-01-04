from importlib import import_module

from inspect import getmembers, isclass, isabstract

from facade.facade.get_employees.abs_facade import AbsFacade


class FacadeFactory:
    @staticmethod
    def create_facade(module_name):
        module = import_module('.' + module_name, __package__)
        classes = getmembers(module, predicate=lambda member: (
                    isclass(member) and not isabstract(module) and issubclass(member, AbsFacade)))
        return classes[0][1]()

