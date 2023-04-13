#!/bin/tcsh

foreach i (2.50 2.60 2.70 2.80 2.90 3.00 3.05 3.10 3.15 3.20 3.22 3.25 3.26 3.27 3.28 3.29 3.30 3.31 3.32 3.33 3.34 3.35 3.36 3.37 3.38 3.39 3.40 3.42 3.45 3.50 3.60 3.70 3.80 3.90 4.00 4.20 4.40 4.60 4.80 5.00 5.50 6.00 6.50 7.00 )

set k=`echo $i`

set ext = `echo $i | sed 's/\./_/'`

mkdir $ext
cp control.in $ext/.

cat > $ext/geometry.in << EOF 
lattice_vector         2.46670923        0.00000000        0.00000000
lattice_vector         1.23286602        2.13599798        0.00000000
lattice_vector         0.00000000        0.00000000        40.00
atom      -0.6165934086165   -0.35599823933468      0.00000000      C
atom       0.6165934086165    0.35599823933468      0.00000000      C
atom       1.849787625        1.06799899            $k              C
atom       3.08297814180825   1.77999760466734      $k              C

EOF

cat > $ext/submit.sh <<EOF
#!/bin/bash
#SBATCH -A batch
#SBATCH -N 1
#SBATCH -n 20
#SBATCH --time=06:00:00
#SBATCH -J aims

export OMP_NUM_THREADS=1

module load openmpi
module load scalapack/2.0.2
module load blacs/2.0.2-7
module load gcc/4.9.3

mpirun ../../../bin/aims.150620.scalapack.mpi.x > Graphene_Bulk$ext.out

EOF

cd $ext
sbatch submit.sh

cd ../

end

