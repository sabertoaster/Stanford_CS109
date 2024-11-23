import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv('music.csv')

# Function to calculate probabilities
def calculate_probability(condition):
    return len(df[condition]) / len(df)

# Function to calculate expected value
def calculate_expected_value(column):
    return df[column].mean()

# Function to calculate covariance
def calculate_covariance(col1, col2):
    return np.cov(df[col1], df[col2])[0][1]

# a. P(R_Folk = 5)
p_folk_5 = calculate_probability(df['Folk'] == 5)

# b. P(R_Folk = x)
def p_folk_x(x):
    return calculate_probability(df['Folk'] == x)

# c. E[R_Musical]
e_musical = calculate_expected_value('Musical')

# d. P(R_Folk = 5 | R_Musical = 5)
p_folk_5_given_musical_5 = calculate_probability((df['Folk'] == 5) & (df['Musical'] == 5)) / calculate_probability(df['Musical'] == 5)

# e. P(R_Folk = x | R_Musical = 5)
def p_folk_x_given_musical_5(x):
    return calculate_probability((df['Folk'] == x) & (df['Musical'] == 5)) / calculate_probability(df['Musical'] == 5)

# f. Covariance of R_Opera and R_Punk
cov_opera_punk = calculate_covariance('Opera', 'Punk')

# Print results
print(f"a. P(R_Folk = 5) = {p_folk_5:.4f}")
print(f"b. P(R_Folk = x) is a function, call p_folk_x(x) with x = 1 to 5")
print(f"c. E[R_Musical] = {e_musical:.4f}")
print(f"d. P(R_Folk = 5 | R_Musical = 5) = {p_folk_5_given_musical_5:.4f}")
print(f"e. P(R_Folk = x | R_Musical = 5) is a function, call p_folk_x_given_musical_5(x) with x = 1 to 5")
print(f"f. Covariance of R_Opera and R_Punk = {cov_opera_punk:.4f}")