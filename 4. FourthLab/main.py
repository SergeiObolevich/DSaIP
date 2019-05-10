import transform as tr
import matplotlib.pyplot as plt


def main():
    max_decomposition_depth = 4
    data = [6, 10, 6, 1, 2, 7, 13, 4, 12, 10, 8, 11, 10, 6, 13, 12]
    length = len(data)
    arguments = [i for i in range(1, len(data) + 1)]

    wavelet_transform_result = tr.fwt(data, max_decomposition_depth)
    inverse_wavelet_results = []
    for i in range(max_decomposition_depth):
        inverse_wavelet_results.append(tr.inverse_fwt(wavelet_transform_result, i + 1))

    for i in range(max_decomposition_depth):
        extended_result = []
        for x in inverse_wavelet_results[i]:
            extended_result += [x for i in range(int(length / len(inverse_wavelet_results[i])))]

        inverse_wavelet_results[i] = extended_result

    print(wavelet_transform_result)
    print(inverse_wavelet_results[0])

    _, ((plot1, plot2), (plot3, plot4), (plot5, plot6)) = plt.subplots(3, 2)

    plot1.plot(arguments, data)
    plot1.set(title='Initial signal')
    plot1.grid()

    plot2.plot(arguments, wavelet_transform_result)
    plot2.set(title='FWT filters arguments')
    plot2.grid()

    plot3.plot(arguments, inverse_wavelet_results[0])
    plot3.set(title='Inverse FWT level 1 signal')
    plot3.grid()

    plot4.plot(arguments, inverse_wavelet_results[1])
    plot4.set(title='Inverse FWT level 2 signal')
    plot4.grid()

    plot5.plot(arguments, inverse_wavelet_results[2])
    plot5.set(title='Inverse FWT level 3 signal')
    plot5.grid()

    plot6.plot(arguments, inverse_wavelet_results[3])
    plot6.set(title='Inverse FWT level 4 signal')
    plot6.grid()

    plt.show()


if __name__ == '__main__':
    main()
