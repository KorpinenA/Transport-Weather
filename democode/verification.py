import numpy as np
from democode import tools as tl
from democode import plotting as pl


def main():
    dataF, dataO = tl.get_data_frame()
    stations = tl.find_same_stations(dataF, dataO)
    dataF, dataO = tl.initialize_case(stations[0], dataF, dataO)
    tsF, tsO = tl.separate_season('summer', dataF, dataO)
    taF, taO = tl.separate_season('autumn', dataF, dataO)
    twF, twO = tl.separate_season('winter', dataF, dataO)
    tkF, tkO = tl.separate_season('spring', dataF, dataO)


    day_time = np.arange(0, 24, 1)

    # TimeSeries
    pl.timeseries(dataF['fctime'], dataO['time'], dataF['temp_r'], dataO['temp_r'])

    # Histogram
    pl.histogram(tsF, tsO, taF, taO, twF, twO, tkF, tkO)

    # histogram day night
    dataF_d, dataF_n, dataO_d, dataO_n = tl.separate_day_night(dataF, dataO)
    for dfF, dfO, title in zip([dataF_d, dataO_d],[dataF_n, dataO_n],['Day', 'Night']):
        tsF_s, tsO_s = tl.separate_season('summer', dfF, dfO)
        taF_s, taO_s = tl.separate_season('autumn', dfF, dfO)
        twF_s, twO_s = tl.separate_season('winter', dfF, dfO)
        tkF_s, tkO_s = tl.separate_season('spring', dfF, dfO)
        pl.histogram(tsF_s, tsO_s, taF_s, taO_s, twF_s, twO_s, tkF_s, tkO_s, title)

    # Hourly averages
    tsF_h, tsO_h = tl.average_hour(tsF, tsO, 'temp_r')
    taF_h, taO_h = tl.average_hour(taF, taO, 'temp_r')
    twF_h, twO_h = tl.average_hour(twF, twO, 'temp_r')
    tkF_h, tkO_h = tl.average_hour(tkF, tkO, 'temp_r')
    pl.hourly_timeseries(day_time, tsF_h, tsO_h, taF_h, taO_h, twF_h, twO_h, tkF_h, tkO_h)




if __name__ == "__main__":
    main()
