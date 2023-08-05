import os
from statistics import mean


def calc_average(values):
    float_values = []
    for raw_value in values:
        float_value = float(raw_value)
        float_values.append(float_value)

    average = mean(float_values)
    round_average = round(average, 2)
    return round_average


with open(os.path.join('testFiles', 'temperature.txt'), mode='r') as file:
    content = file.read()
    lines = content.splitlines()
    print(lines)

average_value = calc_average(lines)
print(f'Average value: {average_value}')

with open(os.path.join('testData', 'temperature_avr.txt'), mode='a+') as file_1:
    file_1.writelines([str(average_value), '\n'])
    print("Average saved")
