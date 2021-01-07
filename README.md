# mpi2
Practica 2 de MPI

mpicc test_banda_ancha.c –o tba


mpirun -n 2 -hostfile hostfile.txt test_banda_ancha


scp -r "C:\Users\cochoa\Documents\Unizar\Periodo 3\Computacion de altas prestaciones\MPI\mpi2" a792900@hendrix.cps.unizar.es:/home/a792900/Documents/MPI

scp a792900@hendrix.cps.unizar.es:/home/a792900/Documents/MPI/mpi2/mihostfile.txt "C:\Users\cochoa\Documents\Unizar\Periodo 3\Computacion de altas prestaciones\MPI\mpi2"


-mca btl_tcp_if_include br0