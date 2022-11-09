from abc import ABC, abstractmethod


class CameraSystem:
    """Централизованная система наблюдения."""

    def __init__(self):
        self.__observers = set()

    # Подключить наблюдателя(камеру) к системе. (просто добавляем объект в список).
    def attach(self, observer):
        self.__observers.add(observer)

    # Отключить наблюдателя(камеру) от системы. (просто удаляем объект из список).
    def detach(self, observer):
        self.__observers.remove(observer)

    # Отправка уведомления\команды всем наблюдателям(камерам) подключенным к системе.
    # (Проходимся по списку объектов и вызываем нужный метод).
    def notify(self):
        for observer in self.__observers:
            observer.make_photo()


# Абстрактный класс наблюдателя.
# Косвенно указывает какие методы необходимо реализовать в его наследниках.
# Ведь в дальнейшем мы можем подключить к центральной системе не только камеры, но и например автоматические пулеметы ))
class AbstractObserver(ABC):
    @abstractmethod
    def make_photo(self):  # Абстрактный наблюдатель задает метод make_photo
        pass


class Camera(AbstractObserver):
    """Камера наблюдения."""

    def __init__(self, name):
        self.name = name

    def make_photo(self):
        print('{} сделала фото'.format(self.name))


n = CameraSystem()
c1 = Camera('Camera 1')
c2 = Camera('Camera 2')
c3 = Camera('Camera 3')
n.attach(c1)
n.attach(c2)
n.attach(c3)
n.notify()
n.detach(c2)
n.notify()
