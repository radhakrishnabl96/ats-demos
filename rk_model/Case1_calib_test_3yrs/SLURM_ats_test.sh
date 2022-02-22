#!/bin/bash -l
#SBATCH --job-name=test_ats_2
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --ntasks-per-node=1
#SBATCH --ntasks-per-core=1
#SBATCH --mem-per-cpu=2G
#SBATCH --time=00:20:00
#SBATCH --partition=amo
#SBATCH --constraint=[skylake|haswell]
#SBATCH --mail-user=radhakrishna@hydromech.uni-hannover.de
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --output test_ats-job_2%j.out
#SBATCH --error test_ats-job_2%j.err
 
# Change to my work dir
mkdir $SLURM_SUBMIT_DIR/test_slurm_2.demo
cd $SLURM_SUBMIT_DIR/test_slurm_2.demo

# Load modules
 
# Run ats
srun singularity exec /bigwork/nhgjrabl/Singularity/ats_pest_final.sif ats --xml_file=../Case1_B_calib_3yrs.xml &>out.log
