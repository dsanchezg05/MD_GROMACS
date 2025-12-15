import os
import argparse
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--directory", "-d", help='Working directory')
args = parser.parse_args()

dir = args.directory

df=pd.read_csv(f"{dir}/distance.csv", header=None)
print(df.head())
print(df.iloc)
plt.plot(np.array(df.iloc[:,0]), np.array(df.iloc[:,1]))
plt.show()