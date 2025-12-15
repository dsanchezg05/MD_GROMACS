# Molecular Dynamics simulation using GROMACS
To perform a Molecular Dynamics simulation, file **gromacs_pipeline.sh** must be executed with arguments:
$$
bash gromacs_pipeline.sh "input.pdb"
$$
As a result, ".gro" and ".txc" files are created, and mean RMSD between each instance and t=0 model can be represented executing "RMSD_Model.py", with arguments:

$$
python3 rmsd_graph.py --wdir "directory where result files are stored" --tt "graph title"
$$
