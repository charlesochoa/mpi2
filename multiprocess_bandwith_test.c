#include<stdio.h>
#include <stdlib.h>
#include<mpi.h>
#include <sys/time.h>

int main( int argc, char* argv[] ) {
    int this_proc, total_procs;

    /* Aqui comienza el paralelismo */
    MPI_Init( &argc, &argv );
    int np = atoi(argv[1]);
    int psize = atoi(argv[2]);
    int nexp = atoi(argv[3]);
    int sendbuf[psize];
    int recvbuf[psize];
    int ack = 0;
    int size_of_int = sizeof(int);
    double start, end;
    MPI_Comm_size( MPI_COMM_WORLD, &total_procs ); // number of process
    MPI_Comm_rank( MPI_COMM_WORLD, &this_proc );  //PID
    // printf("exp,src,dst,number_of_packets,packet_size,time\n");
    for(int j = 1; j < nexp; j++){
        if (this_proc % 2 == 0) {
            start = MPI_Wtime();
            for (int i = 0; i < np; i++)
            {
                MPI_Send(&sendbuf, psize, MPI_INT, this_proc + 1, 0, MPI_COMM_WORLD);
            }
            MPI_Recv(&ack, 1, MPI_INT, this_proc + 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            end = MPI_Wtime();
            double t_band = end - start;
            printf("%d,%d,%d,%d,%d,%f\n", j, this_proc, this_proc + 1, np, psize * size_of_int, t_band);

        } else
        {
            for (int i = 0; i < np; i++)
            {
                MPI_Recv(&recvbuf, psize, MPI_INT, this_proc - 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            }
            MPI_Send(&ack, 1, MPI_INT, this_proc - 1, 0, MPI_COMM_WORLD);
        }
    }

    MPI_Finalize();
    return 0;
}