from abc import ABCMeta, abstractmethod


class BaseDBRepo(metaclass=ABCMeta):

    @abstractmethod
    def create(self, *args, **kwargs): ...

    @abstractmethod
    def get(self, *args, **kwargs): ...

    @abstractmethod
    def get_all(self, *args, **kwargs): ...

    @abstractmethod
    def delete(self, *args, **kwargs): ...
