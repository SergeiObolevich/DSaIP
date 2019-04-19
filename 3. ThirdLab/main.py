import transform as tr
import numpy as np
import matplotlib.pyplot as plt


def main():
    n = 64
    arguments = np.arange(0, n) * np.pi / 10
    function_values = list(map(lambda x: np.sin(x) + np.cos(x), arguments))

    dwt_result = tr.dwt(function_values, 1)
    fwht_result = tr.fwht(function_values, 1)
    reverse_dwt_result = tr.dwt(dwt_result, -1)
    reverse_fwht_result = tr.fwht(fwht_result, -1)

#    print("Discrete transformation: {}".format(n * n))
#    print("Fast transformation: {}".format(int(n * np.log2(n))))
#    for i in range(n):
#        print(dwt_result[i], ' : ', fwht_result[i])

    _, represent = plt.subplots(3, 2)

    represent[0, 0].plot(arguments, function_values)
    represent[0, 0].set(title='Исходная функция: six(x) + cos(x)')
    represent[0, 0].grid(True)

    represent[0, 1].plot(arguments, function_values)
    represent[0, 1].set(title='Исходная функция: six(x) + cos(x)')
    represent[0, 1].grid(True)

    represent[1, 0].stem(arguments, dwt_result, markerfmt=' ')
    represent[1, 0].set(title='Спектр величин Дискретного преобразования Уолша')
    represent[1, 0].grid(True)

    represent[1, 1].stem(arguments, fwht_result, markerfmt=' ')
    represent[1, 1].set(title='Спектр величин Быстрого преобразования Уолша')
    represent[1, 1].grid(True)

    represent[2, 0].plot(arguments, reverse_dwt_result)
    represent[2, 0].set(title='Обратное Дискретное преобразования Уолша')
    represent[2, 0].grid(True)

    represent[2, 1].plot(arguments, reverse_fwht_result)
    represent[2, 1].set(title='Обратное Быстрое преобразования Уолша')
    represent[2, 1].grid(True)
    plt.show()


if __name__ == '__main__':
    main()
