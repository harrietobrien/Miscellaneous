#!/bin/tcsh
foreach i (2.50 2.60 2.70 2.80 2.90 3.00 3.05 3.10 3.15 3.20 3.22 3.25 3.26 3.27 3.28 3.29 3.30 3.31 3.32 3.33 3.34 3.35 3.36 3.37 3.38 3.39 3.40 3.42 3.45 3.50 3.60 3.70 3.80 3.90 4.00 4.20 4.40 4.60 4.80 5.00 5.50 6.00 6.50 7.00 )

set ext = `echo $i | sed 's/\./_/'`
cd $ext

set Energy=`cat *.out | grep "| Total energy of the DFT / Hartree-Fock s.c.f. calculation      :" | sed 's/^.\{44\}//g' | cut -c 35-49`

echo $i $Energy  >> ../EnergyData.txt
cd ..

end

