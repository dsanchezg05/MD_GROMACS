import os
import argparse
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statistics

parser = argparse.ArgumentParser()
parser.add_argument("--directory", "-d", help='Working directory')
args = parser.parse_args()

dir = args.directory

df=pd.read_csv(f"{dir}/distance.csv", header=None)
print(df.head())
print(df.iloc)
plt.plot(np.array(df.iloc[:,0]), np.array(df.iloc[:,1]))
plt.xlabel("Time")
plt.ylabel("RMSD")
mean_rmsd=statistics.mean(np.array(df.iloc[:,1]))
plt.title(f"Distance Binder vs Target, mean RMSD={round(mean_rmsd,3)}")
plt.show()
