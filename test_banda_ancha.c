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
    int sendbuf[psize];
    int recvbuf[psize];
    int ack = 0;
    struct timeval t1, t2;
    MPI_Comm_size( MPI_COMM_WORLD, &total_procs ); // number of process
    MPI_Comm_rank( MPI_COMM_WORLD, &this_proc );  //PID
    if( this_proc == 0){
        gettimeofday(&t1, NULL);
        for (int i = 0; i < np; i++)
        {
            MPI_Send(&sendbuf, psize, MPI_INT, 1, 0, MPI_COMM_WORLD);
        }
        MPI_Recv(&ack, 1, MPI_INT, 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        gettimeofday(&t2, NULL);
        int t_band = (t2.tv_sec - t1.tv_sec) * 1000000 + t2.tv_usec - t1.tv_usec;
        printf("-- Process [%d] sent %d bursts of size %d to process %d, burst time was %d microseconds.\n", this_proc, np, psize, this_proc + 1, t_band);
        
    } else if (this_proc == 1)
    {
        for (int i = 0; i < np; i++)
        {
            MPI_Recv(&recvbuf, psize, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        }
        MPI_Send(&ack, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
        printf("Done!: Process %d.\n", this_proc);
    }
    

    printf( "Hello word! I'm process nro. %d over a total of %d process.\n", this_proc, total_procs );
    MPI_Finalize();
    return 0;
}