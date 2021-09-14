import numpy as np
from democode import tools as tl


def main():
    dfF, dfO = tl.get_data_frame()
    stations = tl.find_same_stations(dfF, dfO)
    probabilities = {}
    probabilities['neg_yes'] = 0
    probabilities['neg_no'] = 0
    probabilities['plus_yes'] = 0
    probabilities['plus_no'] = 0
    for x, site in enumerate(stations):
        print(site)
        try:
            dataF, dataO = tl.initialize_case(site, dfF, dfO)
            dataO = tl.remove_nan_index(dataO, 'temp_2')
        except:
            continue
        j = 1
        fO_prob = {}
        min = -10
        for i in range(-10, 11, 1):
            try:
                z_prob = tl.get_probability_between(i, min + j, dataO)
            except ZeroDivisionError:
                continue
            j += 1
            fO_prob[i] = np.round(z_prob, 1)

        for t in dataO['time'].values:
            try:
                Tf_2 = dataF['temp_2'].loc[dataF['fctime'] == t].values[0]
                Tf_r = dataO['temp_r'].loc[dataO['time'] == t].values[0]
            except:
                continue

            if Tf_2 < -10:
                t_rf_prob = 1.0
            elif Tf_2 > 10:
                t_rf_prob = 0.0
            else:
                try:
                    t_rf_prob = fO_prob[int(Tf_2)]
                except KeyError:
                    continue
            if Tf_r < 0 and t_rf_prob > 0.5:
                last_n = probabilities['neg_yes']
                probabilities['neg_yes'] = last_n + 1
            if Tf_r < 0 and t_rf_prob < 0.5:
                last_n = probabilities['neg_no']
                probabilities['neg_no'] = last_n + 1
            if Tf_r > 0 and t_rf_prob > 0.5:
                last_n = probabilities['plus_no']
                probabilities['plus_no'] = last_n + 1
            if Tf_r > 0 and t_rf_prob < 0.5:
                last_n = probabilities['plus_yes']
                probabilities['plus_yes'] = last_n + 1
        print("kierros done")
    print("")


if __name__ == "__main__":
    main()
