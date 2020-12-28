/* filename: multiprocess_latency_test.c */
#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <sys/time.h>
 
int main( int argc, char* argv[] ) {
    int this_proc;
    int task_id;
    int i;
    int N; /* N is the number of pairs */
    int M; /* M is the number of bounces */
    struct timeval t1, t2;

    if (argc == 5) {
        i = 1;
        while (i < 5) {
            if (argv[i] == "-N") {
                N = atoi(argv[i]);
                i++;
            } else if (argv[i] == "-M") {
                M = atoi(argv[i]);
                i++;
            }
            i++;
        }
    }
    else {
        printf("Incorrect number of arguments supplied!\n");
    }
 
    MPI_Init(NULL, NULL);
    MPI_Comm_size(MPI_COMM_WORLD, &N); // Number of processes
    MPI_Comm_rank(MPI_COMM_WORLD, &this_proc);   // PID
 
    printf("Hello word! I'm process number %d of %d processes.\n", this_proc, N);

    if (this_proc % 2 == 0) {
        task_id = this_proc;
        gettimeofday(&t1, NULL);
        MPI_Send(&task_id, 1, MPI_INT, this_proc + 1, 0, MPI_COMM_WORLD);
        gettimeofday(&t2, NULL);
        int t_send = (t2.tv_sec - t1.tv_sec) * 1000000 + t2.tv_usec - t1.tv_usec;
        printf("-- Process [%d] sent task id %d to process %d, send time was %d microseconds.\n", this_proc, task_id, this_proc + 1, t_send);
    } else {
        gettimeofday(&t1, NULL);
        MPI_Recv(&task_id, 1, MPI_INT, this_proc - 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        gettimeofday(&t2, NULL);
        int t_recv = (t2.tv_sec - t1.tv_sec) * 1000000 + t2.tv_usec - t1.tv_usec;
        printf("-- Process [%d] received task id %d from process [%d], receive time was %d microseconds.\n", this_proc, task_id, this_proc - 1, t_recv);
    };

    MPI_Finalize();
    return 0; 
}