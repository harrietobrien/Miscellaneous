#!/bin/bash

MPIRUN=/usr/lib64/openmpi/bin/mpirun
NODES=25
SCALAPACKBIN=~/fhi-aims.160328_3/bin/aims.160328_3.scalapack.mpi.x

$MPIRUN -n $NODES $SCALAPACKBIN > aims.out