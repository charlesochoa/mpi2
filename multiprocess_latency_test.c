/* filename: multiprocess_latency_test.c */
#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <string.h>
 
int main(int argc, char* argv[]) {
    int this_proc;
    int i;
    int n;      /* number of pairs */
    int m = -1; /* number of bounces */
    int p = -1; /* size of the packets */
    int size_of_int;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &n);           // number of processes
    MPI_Comm_rank(MPI_COMM_WORLD, &this_proc);   // PID

    i = 0;
    while (i < argc) {
        if (strcmp(argv[i], "-p") == 0) {
            p = atoi(argv[i+1]);
            i++;
        } else if (strcmp(argv[i], "-m") == 0) {
            m = atoi(argv[i+1]);
            i++;
        }
        i++;
    }
            
    if ((m < 0) || (p < 0)) {
        printf("Missing argument for number of bounces or the size of the packets!\n");
        MPI_Finalize();
        return 0;
    }

    if (n % 2 != 0) {
        printf("Number of processes must be even!\n");
        MPI_Finalize();
        return 0;
    }
 
    printf("Hello word! I'm process number %d of %d processes.\n", this_proc, n);

    // Packet
    int sendbuffer[p];
    int recvbuffer[p];

    int size_of_int = sizeof(int);

    if (this_proc % 2 == 0) {
        for (i = 0; i < m; i++) {
            // ********************** SEND **********************
            start = MPI_Wtime();
            MPI_Send(sendbuffer, p, MPI_INT, this_proc + 1, 0, MPI_COMM_WORLD);
            end = MPI_Wtime();
            double t_send = end - start;
            printf("-- Bounce number [%d] * Process [%d] sent packet of size %d to process [%d], send time was %f seconds.\n", i, this_proc, p * size_of_int, this_proc - 1, t_send);

            // ********************** RECEIVE **********************
            start = MPI_Wtime();
            MPI_Recv(recvbuffer, p, MPI_INT, this_proc + 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            end = MPI_Wtime();
            double t_recv = end - start;
            printf("-- Bounce number [%d] * Process [%d] received packet of size %d from process [%d], receive time was %f seconds.\n", i, this_proc, p * size_of_int, this_proc + 1, t_recv);
        }
    } else {
        for (i = 0; i < m; i++) {
            // ********************** RECEIVE **********************
            start = MPI_Wtime();
            MPI_Recv(recvbuffer, p, MPI_INT, this_proc - 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            end = MPI_Wtime();
            double t_recv = end - start;
            printf("-- Bounce number [%d] * Process [%d] received packet of size %d from process [%d], receive time was %f seconds.\n", i, this_proc, p * size_of_int, this_proc + 1, t_recv);

            // ********************** SEND **********************
            start = MPI_Wtime();
            MPI_Send(sendbuffer, p, MPI_INT, this_proc - 1, 0, MPI_COMM_WORLD);
            end = MPI_Wtime();
            double t_send = end - start;
            printf("-- Bounce number [%d] * Process [%d] sent packet of size %d to process [%d], send time was %f seconds.\n", i, this_proc, p * size_of_int, this_proc - 1, t_send);
        }
    };

    MPI_Finalize();
    return 0;
}