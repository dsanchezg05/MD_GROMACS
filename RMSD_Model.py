import os
#import plotly.express as px
import matplotlib.pyplot as plt
import argparse
#import pandas as pd
import numpy as np
import statistics
parser=argparse.ArgumentParser()
parser.add_argument('--wdir', '-w' , type=str, help='Absloute working dir')
parser.add_argument('--tt', '-t' , type=str, help='Title for graph')
args=parser.parse_args()

dir=args.wdir
tlt=args.tt

try:
    assert(os.path.isfile(f"{dir}/rmsd.xvg") == True)
    x, y = np.loadtxt(f"{dir}/rmsd.xvg", comments=["@", "#", "&"], unpack=True)
    plt.plot(x, y)
    plt.xlabel("Time")
    plt.ylabel("RMSD")
    mean_rmsd=statistics.mean(y)
    plt.title(f"{tlt},mean RMSD={round(mean_rmsd,3)}")
    plt.show()
except:
    print("RMSD file not found")

