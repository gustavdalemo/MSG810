import csv
import random
import numpy as np
import matplotlib.pyplot as plt

# Ange medelvärde och standardavvikelse för IQ-fördelningen
mean = 100
std_dev = 15

# Generera slumpmässiga IQ-värden för en population
population_size = 10000000  # Antal personer i populationen
iq_population = np.random.normal(mean, std_dev, population_size)


def sampleMedianIQ(sampleSize, population):
    sample_population = population[:sampleSize]
    median = 0
    for element in sample_population:
        median += element
    median = median/sampleSize
    return (median, sample_population)



def create_hist_diagram(population):
    n = len(population)
    plt.hist(population, bins=n)
    plt.xlabel('IQ')
    plt.ylabel('Frequency')
    plt.title('IQ Distribution Histogram')

    plt.show()


def create_bar_chart():
    y_values = iq_population
    x_values = range(len(y_values))

    plt.bar(x_values,y_values)

    plt.xticks(x_values, map(int, x_values))

    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Chart')

    plt.show()

(median, sample_population) = sampleMedianIQ(1000, iq_population)
print(sample_population)
print("Median: ", median)


# Saving data into file
fields = ['IQ']

with open('data.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerow(sample_population)


#create_bar_chart()
create_hist_diagram(sample_population)