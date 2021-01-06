#!/bin/bash

mpicc multiprocess_latency_test.c -o multiprocess_latency_test.o

for i in 1 10 100
do
   echo "Running multiprocess_latency_test..."
   mpirun -n 8 --hostfile mihostfile.txt -mca btl_tcp_if_include br0 ./multiprocess_latency_test.o -m 100 -p $i >> multiprocess_latency_test.csv 
done