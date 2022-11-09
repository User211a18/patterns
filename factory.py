import math


class Sin_x:
    def __init__(self, x):
        self.x = x
        x = x / 180 * math.pi

    def __str__(self):
        return f'sin(x)={self.x}'


class FunctionFactory:
    @staticmethod
    def Function(x):
        return Sin_x(math.sin(x))

    @staticmethod
    def Taylor(x):
        # погрешность
        n = 0.0001
        # сразу берём x как первое слагаемое ряда Тейлора
        q = x
        # сумма ряда на старте равна нулю
        s = 0
        # порядковый номер слагаемого в ряду Тейлора
        i = 1

        # пока очередное слагаемое больше погрешности — цикл работает
        while abs(q) > n:
            # добавляем слагаемое к общей сумме
            s = s + q
            # вычисляем следующее слагаемое
            q = q * (-1) * (x * x) / ((2 * i + 1) * (2 * i))
            # увеличиваем порядковый номер слагаемого в ряду Тейлора
            i = i + 1
            # возвращаем сумму как результат работы функции
        return Sin_x(s)
print(FunctionFactory.Function(30))
print(FunctionFactory.Taylor(30))