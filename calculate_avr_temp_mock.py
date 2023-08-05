from statistics import mean


def calc_average(values):
    float_values = []
    for raw_value in values:
        float_value = float(raw_value)
        float_values.append(float_value)

    average = mean(float_values)
    round_average = round(average, 2)
    print(round_average)


file_data_mock = ['20.1', '21.2', '22.1']
calc_average(file_data_mock)
