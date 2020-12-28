/* filename: multiprocess_latency_test.c */
#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <sys/time.h>
#include <string.h>
 
int main(int argc, char* argv[]) {
    int this_proc;
    int task_id;
    int i;
    int n; /* n is the number of pairs */
    int m = -1; /* m is the number of bounces */
    int p = -1;
    struct timeval t1, t2;
 
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &n);           // Number of processes
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
        printf("Missing argument for number of bounces or size of packages!\n");
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

    if (this_proc % 2 == 0) {
        for (i = 0; i < m; i++) {
            // ********************** SEND **********************
            gettimeofday(&t1, NULL);
            MPI_Send(sendbuffer, p, MPI_INT, this_proc + 1, 0, MPI_COMM_WORLD);
            gettimeofday(&t2, NULL);
            int t_send = (t2.tv_sec - t1.tv_sec) * 1000000 + t2.tv_usec - t1.tv_usec;
            printf("-- Bounce number [%d] * Process [%d] sent task id %d to process %d, send time was %d microseconds.\n", i, this_proc, task_id, this_proc + 1, t_send);
        
            // ********************** RECEIVE **********************
            gettimeofday(&t1, NULL);
            MPI_Recv(recvbuffer, p, MPI_INT, this_proc + 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            gettimeofday(&t2, NULL);
            int t_recv = (t2.tv_sec - t1.tv_sec) * 1000000 + t2.tv_usec - t1.tv_usec;
            printf("-- Bounce number [%d] * Process [%d] received task id %d from process [%d], receive time was %d microseconds.\n", i, this_proc, task_id, this_proc + 1, t_recv);
        }
    } else {
        for (i = 0; i < m; i++) {
            // ********************** RECEIVE **********************
            gettimeofday(&t1, NULL);
            MPI_Recv(recvbuffer, p, MPI_INT, this_proc - 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            gettimeofday(&t2, NULL);
            int t_recv = (t2.tv_sec - t1.tv_sec) * 1000000 + t2.tv_usec - t1.tv_usec;
            printf("-- Bounce number [%d] * Process [%d] received task id %d from process [%d], receive time was %d microseconds.\n", i, this_proc, task_id, this_proc - 1, t_recv);
        
            // ********************** SEND **********************
            gettimeofday(&t1, NULL);
            MPI_Send(sendbuffer, p, MPI_INT, this_proc - 1, 0, MPI_COMM_WORLD);
            gettimeofday(&t2, NULL);
            int t_send = (t2.tv_sec - t1.tv_sec) * 1000000 + t2.tv_usec - t1.tv_usec;
            printf("-- Bounce number [%d] * Process [%d] sent task id %d to process %d, send time was %d microseconds.\n", i, this_proc, task_id, this_proc - 1, t_send);

        }
    };

    MPI_Finalize();
    return 0;
}