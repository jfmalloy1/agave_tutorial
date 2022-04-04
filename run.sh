#!/bin/bash

# #SBATCH --mem 120GB
#SBATCH -n 1
#SBATCH -c 4
#SBATCH -J Agave_Tutorial
#SBATCH -o slurm.agaveTutorial.out
#SBATCH -e slurm.agaveTutorial.err
#SBATCH -t 12:01:30
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jmalloy3@asu.edu

module purge
module load anaconda/py3
module load rclone/1.43
module load gcc/11.2.0

eval $"source activate my-rdkit-env"

python parallel.py
