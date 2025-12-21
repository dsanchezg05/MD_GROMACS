import os
import numpy as np
import argparse
import statistics
from tqdm import tqdm
import matplotlib.pyplot as plt
import statistics

parser = argparse.ArgumentParser()
parser.add_argument("--directory", "-d", help='Working directory with PDB file')
args = parser.parse_args()

dir = args.directory

with open(dir, "r") as f:
    read=f.readlines()

with open(dir,"r") as f:
    rd=f.read()
reps=rd.count("END")
print(f"Timestamp: {reps}")
cycles=0
for i in read:
    if i == "END\n": break
    else: cycles=cycles+1 
print(f"Residues: {cycles}")
rmsd=[]; counter=0
for time in tqdm(range(1, reps)):
    counter=counter+1;dist=[]
    for res in range(1,cycles):
        x=[];xx=[]
        line=read[res]
        new_l=read[(time*cycles)+res]
        for i in line.split(" "):
            if i != "": x.append(i)
        for i in new_l.split(" "):
            if i != "": xx.append(i)

        #print(x)
        l=x[6:9]
        #print(xx)
        nl=xx[6:9]
        #print(l)
        #print(nl)
        dist.append(abs(float(nl[0])-float(l[0]))+abs(float(nl[1])-float(l[1]))+abs(float(nl[2])-float(l[2])))
        #print(dist)
        #break
    res_dist=statistics.mean(dist)
    rmsd.append(np.sqrt(res_dist))
    #print(f"RMSD Res: {counter} = {rmsd[-1]}")
    #break
        

plt.plot(range(1,reps), rmsd)
plt.xlabel("Time")
plt.ylabel("RMSD")
mean_rmsd=statistics.mean(rmsd)
plt.title(f"Distance between binder positions, mean RMSD={round(mean_rmsd,3)}")
plt.show()
