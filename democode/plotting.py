import matplotlib.pyplot as plt
import democode.tools as tl


def timeseries(tF, tO, TF_road, TO_road):
    TF_road_mean = tl.calculate_average(TF_road, 24)
    TO_road_mean = tl.calculate_average(TO_road, 24)

    plt.title('Road temperature of Forecast vs. Observation')
    plt.subplot(2, 1, 1)
    plt.grid(axis='y')
    plt.plot(tF[::12], TF_road[::12], label='Forecast')
    plt.plot(tO[::12], TO_road[::12], label='Observation')
    plt.title('Raw, 12h sampling')

    plt.ylabel('Temperature °C')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.grid(axis='y')
    plt.plot(tF[24::24], TF_road_mean, label='Forecast mean')
    plt.plot(tO[24::24], TO_road_mean, label='Observation mean')
    plt.title('Day average')

    plt.ylabel('Temperature °C')

    plt.legend()
    plt.show()


def hourly_timeseries(t, summerF, summerO, autumnF, autumnO, winterF, winterO, springF, springO):
    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
    fig.suptitle('Average hourly mean')

    axs[0, 0].set_title('Summer')
    axs[0, 0].set_ylabel('Temperature °C')
    axs[0, 0].plot(t, summerF, label='Forecast')
    axs[0, 0].plot(t, summerO, label='Observation')
    axs[0, 0].grid()

    axs[0, 1].set_title('Autumn')
    axs[0, 1].plot(t, autumnF, label='Forecast')
    axs[0, 1].plot(t, autumnO, label='Observation')
    axs[0, 1].grid()

    axs[1, 0].set_title('Winter')
    axs[1, 0].set_ylabel('Temperature °C')
    axs[1, 0].set_xlabel('Hour')
    axs[1, 0].plot(t, winterF, label='Forecast')
    axs[1, 0].plot(t, winterO, label='Observation')
    axs[1, 0].grid()

    axs[1, 1].set_title('Spring')
    axs[1, 1].set_xlabel('Hour')
    axs[1, 1].plot(t, springF, label='Forecast')
    axs[1, 1].plot(t, springO, label='Observation')
    axs[1, 1].grid()

    plt.legend()
    plt.show()


def histogram(summerF, summerO, autumnF, autumnO, winterF, winterO, springF, springO, title=''):
    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
    fig.suptitle(title)

    axs[0, 0].set_title('Summer')
    axs[0, 0].set_ylabel('%')
    summerF['temp_r'].hist(bins=11, density=True, alpha=0.7, label='Forecast', ax=axs[0, 0])
    summerO['temp_r'].hist(bins=11, density=True, alpha=0.7, label='Observation', ax=axs[0, 0])

    axs[0, 1].set_title('Autumn')
    autumnF['temp_r'].hist(bins=11, density=True, alpha=0.7, label='Forecast', ax=axs[0, 1])
    autumnO['temp_r'].hist(bins=11, density=True, alpha=0.7, label='Observation', ax=axs[0, 1])

    axs[1, 0].set_title('Winter')
    axs[1, 0].set_ylabel('%')
    axs[1, 0].set_xlabel('°C')
    winterF['temp_r'].hist(bins=11, density=True, alpha=0.7, label='Forecast', ax=axs[1, 0])
    winterO['temp_r'].hist(bins=11, density=True, alpha=0.7, label='Observation', ax=axs[1, 0])

    axs[1, 1].set_title('Spring')
    axs[1, 1].set_xlabel('°C')
    springF['temp_r'].hist(bins=11, density=True, alpha=0.7, label='Forecast', ax=axs[1, 1])
    springO['temp_r'].hist(bins=11, density=True, alpha=0.7, label='Observation', ax=axs[1, 1])

    plt.legend()
    plt.show()
