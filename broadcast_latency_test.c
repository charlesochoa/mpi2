/* filename: broadcast_latency_test.c */
#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <string.h>

void my_broadcast(int rank, int total_processes, int p, int size_of_int) {
    // Packet
    int sendbuffer[p];
    int recvbuffer[p];

    if (rank == 0) {
        for (int i = 1; i < total_processes; i++) {
            MPI_Send(sendbuffer, p, MPI_INT, i, 0, MPI_COMM_WORLD);
        }
    } else {
        MPI_Recv(recvbuffer, p, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
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

    start = MPI_Wtime();
    MPI_Bcast(sendbuffer, p, MPI_INT, 0, MPI_COMM_WORLD);
    end = MPI_Wtime();
    double t_bcast = end - start;
    // version,dst,packet_size,time
    printf("MPI_Bcast,%d,%d,%f\n", rank, p * size_of_int, t_bcast);

    start = MPI_Wtime();
    my_broadcast(rank, n, p, size_of_int);
    end = MPI_Wtime();
    double t_bcast = end - start;
    // version,dst,packet_size,time
    printf("my_broadcast,%d,%d,%f\n", rank, p * size_of_int, t_my_bcast);

    MPI_Finalize();
    return 0;
}
