import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import numpy as np


def load_data(db_file):
    conn = sqlite3.connect(db_file)
    query = "SELECT * FROM data_records"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def basic_statistics(df):
    print(df.describe())
    print(df.info())

def plot_time_series(df):
    df['time'] = pd.to_datetime(df['time'])  
    plt.figure(figsize=(12, 8))
    plt.subplot(311)
    plt.plot(df['time'], df['factor'], label='Factor')
    plt.title('Factor over Time')
    plt.legend()

    plt.subplot(312)
    plt.plot(df['time'], df['pi'], label='Pi', color='r')
    plt.title('Pi over Time')
    plt.legend()

    plt.subplot(313)
    plt.plot(df['time'], df.index, label='Record Index (Time)', color='g')
    plt.title('Record Index over Time')
    plt.legend()

    plt.tight_layout()
    plt.show()

def add_log_columns(df):
    """Add logarithmic columns to the DataFrame for both factor and pi deviation."""
    # Use a small constant to avoid log(0) which is undefined
    df['log_factor'] = np.log(df['factor'].replace(0, np.finfo(float).eps).astype(float))
    df['log_pi_deviation'] = np.log(df['pi_deviation'].replace(0, np.finfo(float).eps))
    return df

def add_pi_deviation(df):
    """Add a column to the DataFrame for the deviation of pi from the true value of pi."""
    true_pi = np.pi  # Accurate pi value from numpy
    df['pi_deviation'] = df['pi'].apply(lambda x: abs(x - true_pi))
    return df

def plot_log_transformations(df):
    """Plot logarithmically transformed factor against pi deviation."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='log_factor', y='log_pi_deviation', data=df)
    sns.regplot(x='log_factor', y='log_pi_deviation', data=df, scatter=False, color='red')  # Regression line
    plt.title('Logarithmic Factor vs. Logarithmic Pi Deviation')
    plt.xlabel('Log(Factor)')
    plt.ylabel('Log(Pi Deviation)')
    plt.show()

def calculate_log_correlation(df):
    """Calculate and print the Pearson correlation coefficient for the logarithmically transformed data."""
    correlation, _ = pearsonr(df['log_factor'], df['log_pi_deviation'])
    print(f"The Pearson correlation coefficient between log(factor) and log(pi deviation) is: {correlation}")

    
# Usage
db_file = 'prj-data.db'
df = load_data(db_file)
basic_statistics(df)
plot_time_series(df)
df = add_pi_deviation(df)  
df = add_log_columns(df)
plot_log_transformations(df)
calculate_log_correlation(df)
