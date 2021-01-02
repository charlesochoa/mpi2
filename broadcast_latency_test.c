/* filename: broadcast_latency_test.c */
#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <string.h>

void my_broadcast(int rank, int total_processes, int p, int size_of_int) {
    // Packet
    int sendbuffer[p];
    int recvbuffer[p];
    double start;
    double end;

    if (rank == 0) {
        for (int i = 1; i < total_processes; i++) {
            // ********************** SEND **********************
            start = MPI_Wtime();
            MPI_Send(sendbuffer, p, MPI_INT, i, 0, MPI_COMM_WORLD);
            end = MPI_Wtime();
            double t_send = end - start;
            printf("-- Process [%d] sent packet of size %d bytes to process [%d], send time was %f seconds.\n", rank, p * size_of_int, i, t_send);
        }
    } else {
        // ********************** RECEIVE **********************
        start = MPI_Wtime();
        MPI_Recv(recvbuffer, p, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        end = MPI_Wtime();
        double t_recv = end - start;
        printf("-- Process [%d] received packet of size %d bytes from process [%d], receive time was %f seconds.\n", rank, p * size_of_int, 0, t_recv);
    }
}
 
int main(int argc, char* argv[]) {
    int rank;
    int i;
    int n;      /* number of pairs */
    int p = -1; /* size of the packets */
    int size_of_int = sizeof(int);
    double start;
    double end;
 
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &n);      // number of processes
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);   // PID

    i = 0;
    while (i < argc) {
        if (strcmp(argv[i], "-p") == 0) {
            p = atoi(argv[i+1]);
            i++;
        }
        i++;
    }
            
    if (p < 0) {
        printf("Missing the size of the packets argument!\n");
        MPI_Finalize();
        return 0;
    }

    // Packet
    int sendbuffer[p];

    printf("******* MPI_Bcast results:\n");
    start = MPI_Wtime();
    MPI_Bcast(sendbuffer, p, MPI_INT, 0, MPI_COMM_WORLD);
    end = MPI_Wtime();
    double t_bcast = end - start;
    printf("-- Process [%d] received a broadcast packet of size %d bytes from process [0], broadcast time was %f seconds.\n", rank, p * size_of_int, t_bcast);

    printf("******* My broadcast results:\n");
    my_broadcast(rank, n, p, size_of_int);

    MPI_Finalize();
    return 0;
}