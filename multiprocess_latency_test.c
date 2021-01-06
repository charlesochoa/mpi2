/* filename: multiprocess_latency_test.c */
#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <string.h>
 
int main(int argc, char* argv[]) {
    int rank;
    int i;
    int n;      /* number of pairs */
    int m = -1; /* number of bounces */
    int p = -1; /* size of the packets */
    int size_of_int = sizeof(int);
    double start, end;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &n);      // number of processes
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);   // PID

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

    // Packet
    int sendbuffer[p];
    int recvbuffer[p];

    start = MPI_Wtime();
    if (rank % 2 == 0) {
        for (i = 0; i < m; i++) {
            // ********************** SEND **********************
            start = MPI_Wtime();
            MPI_Send(sendbuffer, p, MPI_INT, rank + 1, 0, MPI_COMM_WORLD);
            // ********************** RECEIVE **********************
            MPI_Recv(recvbuffer, p, MPI_INT, rank + 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            end = MPI_Wtime();
            double t_bounce = end - start;
            printf("%d,%d,%d,%d,%f\n", i, rank, rank +1, p * size_of_int, t_bounce);
        }
    } else {
        for (i = 0; i < m; i++) {
            // ********************** RECEIVE **********************
            MPI_Recv(recvbuffer, p, MPI_INT, rank - 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            // ********************** SEND **********************
            MPI_Send(sendbuffer, p, MPI_INT, rank - 1, 0, MPI_COMM_WORLD);
        }
    };
    end = MPI_Wtime();
    double t_exec = end - start;

    MPI_Finalize();
    return 0;
}