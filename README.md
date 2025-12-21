# Molecular Dynamics simulation using GROMACS
To perform a Molecular Dynamics simulation, file **gromacs_pipeline.sh** must be executed with arguments:

- bash gromacs_pipeline.sh "input.pdb"


As a result, ".gro" and ".txc" files are created, and mean RMSD between each instance and t=0 model can be represented executing "RMSD_Model.py", with arguments:

- python3 rmsd_graph.py --wdir "directory where result files are stored" --tt "graph title"


RMSD_Binder.py can be executed to detemrine the displacement of a specific chain, from its PDB coordinates file, following the next prompt:

- python3 RMSD_Binder.py -d "path to PDB coordinates file"


distance_BinderTarget.py can be executed to compute the distance between two chains for every timestamp, followng the next prompt after **distance.tcl** is executed and file **distance.csv** is generated:

- source distance.tcl && distance "residues chain A" "residues chain B" "number of bins" distance.csv histogram.csv

- python distance_BinderTarget.py -d "Directory where distance.csv is stored"
