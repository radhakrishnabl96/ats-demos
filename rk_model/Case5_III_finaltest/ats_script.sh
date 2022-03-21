#!/bin/bash -l
#SBATCH --job-name=ats_SWE
#SBATCH --nodes=1
#SBATCH --cpus-per-task=32
#SBATCH --mem-per-cpu=4G
#SBATCH --time=4:00:00
#SBATCH --partition=amo,enos
#SBATCH --constraint=[skylake|haswell]
#SBATCH --output ats_SWE_%j.out
#SBATCH --error ats_SWE_%j.err
 
# Change to my work dir
cd $SLURM_SUBMIT_DIR/Case5_2017_SWE.demo

# Load modules
module load GCCcore/.11.2.0 Python/3.9.6
module load GCC/10.2.0  OpenMPI/4.0.5 SciPy-bundle/2020.11
 
# Run the ats model command within the loop
srun singularity exec /bigwork/nhgjrabl/Singularity/ats_pest_final_2.sif ats --xml_file=../Case5_2017_SWE.xml &>out.log
