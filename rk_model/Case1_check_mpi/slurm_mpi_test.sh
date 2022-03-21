#!/bin/bash -l

#SBATCH --job-name=ats_mpi
#SBATCH --time=00:04:00
#SBATCH --cpus-per-task=32
#SBATCH --output ats_mpi_test_%j.out


# Change to my work dir
cd $SLURM_SUBMIT_DIR/test_ats_cl.demo

# Load modules
module load GCCcore/.11.2.0 Python/3.9.6
module load GCC/10.2.0  OpenMPI/4.0.5 SciPy-bundle/2020.11

export OMPI_MCA_btl_openib_allow_ib=1

# Run the ats model command within the loop
srun singularity exec /bigwork/nhgjrabl/Singularity/ats_pest_final_2.sif ats --xml_file=Case1_mpi_run.xml &>out.log
