#!/bin/bash


dist=(2.50 2.60 2.70 2.80 2.90 3.00 3.05 3.10 3.15 3.20 3.22 3.25 3.26 3.27 3.28 3.29 3.30 3.31 3.32 3.33)
dist=(3.14)
for i in ${dist[@]} 
do
dirname="${i//./_}"  

mkdir $dirname
cp control.in $dirname

cat > $dirname/geometry.in << geometryfile

lattice_vector         2.46670923        0.00000000        0.00000000
lattice_vector         1.23286602        2.13599798        0.00000000
lattice_vector         0.00000000        0.00000000        40.00
atom      -0.6165934086165   -0.35599823933468      0.00000000      C
atom       0.6165934086165    0.35599823933468      0.00000000      C
atom       1.849787625        1.06799899            $i              C
atom       3.08297814180825   1.77999760466734      $i              C

geometryfile


cp control.in $dirname 
cd $dirname
# Change FHI-aims binary call to reflect your binary location 
mpirun -np 1 ~/bin/aims.160328_3.scalapack.mpi.x > "aims$dirname.out" &
cd ../

done
