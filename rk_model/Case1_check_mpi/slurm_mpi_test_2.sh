#!/bin/bash -l

#SBATCH --job-name=ats_mpi_par
#SBATCH --time=00:04:00
#SBATCH --nodes=2
#SBATCH --cpus-per-task=32
#SBATCH --ntasks-per-node=2
#SBATCH --mem-per-cpu=4G
#SBATCH --time=00:04:00
#SBATCH --output ats_mpi_par_%j.out
#SBATCH --error ats_mpi_par__%j.err

# Change to my work dir
cd $SLURM_SUBMIT_DIR/test_ats_cl.demo

# Load modules
module load GCCcore/.11.2.0 Python/3.9.6
module load GCC/10.2.0  OpenMPI/4.0.5 SciPy-bundle/2020.11

export OMPI_MCA_btl_openib_allow_ib=1

# Run the ats model command within the loop
srun singularity exec /bigwork/nhgjrabl/Singularity/ats_pest_final_2.sif ats --xml_file=Case1_mpi_run.xml &>out.log
