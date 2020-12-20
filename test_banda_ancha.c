#include<stdio.h>
#include<mpi.h>

int main( int argc, char* argv[] ) {
    int this_proc, total_procs;

    /* Aqui comienza el paralelismo */
    MPI_Init( &argc, &argv );
    MPI_Comm_size( MPI_COMM_WORLD, &total_procs ); // number of process
    MPI_Comm_rank( MPI_COMM_WORLD, &this_proc );  //PID
    if( this_proc == 0){
        printf("Even: %d", this_proc);
    } else if (this_proc == 1)
    {
        printf("Odd: % d", this_proc);
    }
    

    printf( "Hello word! I'm process nro. %d over a total of %d process.\n", this_proc, total_procs );
    MPI_Finalize();
    return 0;
}