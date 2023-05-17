import random
import numpy as np
import matplotlib.pyplot as plt

# Ange medelvärde och standardavvikelse för IQ-fördelningen
mean = 100
std_dev = 15

# Generera slumpmässiga IQ-värden för en population
size = 1000000
population_size = size  # Antal personer i populationen
iq_population = np.random.normal(mean, std_dev, population_size)

# Skriv ut de första n värdena i populationen
n = 1000000
print(iq_population[:n])
for i in range(len(iq_population)):
    if i < n:
        print(i,iq_population[i])


def create_hist_diagram():
    n = len(iq_population)
    plt.hist(iq_population, bins=n)
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


#create_bar_chart()
create_hist_diagram()