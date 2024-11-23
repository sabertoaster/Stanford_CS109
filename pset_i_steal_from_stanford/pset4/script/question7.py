import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

PATHS = ['personKeyTimingA.txt', 'personKeyTimingB.txt']
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def process_file(path):
    type_duration = []
    prev_time = None

    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            time, key = line.strip().split(",")
            if prev_time is not None:
                type_duration.append(np.round(float(time) - prev_time, 2))
            prev_time = float(time)

    return pd.Series(type_duration)


def plot_histogram(type_duration, title):
    num_samples = len(type_duration)
    hist = type_duration.value_counts().agg(lambda x: x / num_samples * 100).sort_index()
    plt.bar(hist.index, hist.values)
    plt.xlabel('Duration')
    plt.ylabel('Probabilities')
    plt.title(title)
    plt.show()


def calculate_expected_value(type_duration):
    return type_duration.mean()


def calculate_variance(type_duration):
    return type_duration.var()


def display_normal_distribution(type_duration):
    mean = calculate_expected_value(type_duration)
    std = np.sqrt(calculate_variance(type_duration))
    x = np.linspace(mean - 3 * std, mean + 3 * std, 100)
    y = 1 / (std * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mean) / std) ** 2)
    plt.plot(x, y)
    plt.xlabel('Duration')
    plt.ylabel('Probability Density')
    plt.title('Normal Distribution of Typing Durations')
    plt.show()

def approx_normal_distribution_with_histogram(type_duration):
    mean = calculate_expected_value(type_duration)
    std = np.sqrt(calculate_variance(type_duration))
    x = np.linspace(mean - 3 * std, mean + 3 * std, 100)
    y = 1 / (std * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mean) / std) ** 2)
    num_samples = len(type_duration)
    hist = type_duration.value_counts().agg(lambda x: x / num_samples * 100).sort_index()
    plt.bar(hist.index, hist.values, alpha=1, label='Histogram')
    plt.plot(x, y, label='Normal Distribution', color='red')
    plt.xlabel('Duration')
    plt.ylabel('Probabilities')
    plt.title('Approximation of Normal Distribution with Histogram')
    plt.legend()
    plt.show()

PATHS = ['personKeyTimingA.txt', 'personKeyTimingB.txt', 'email.txt']

for path in PATHS:
    type_duration = process_file(path)
    approx_normal_distribution_with_histogram(type_duration)
    print(f'Expected value for {path}: {calculate_expected_value(type_duration):.2f}')
    print(f'Expected value [{path}**2]: {calculate_expected_value(type_duration ** 2):.2f}')
