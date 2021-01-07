mpicc multiprocess_latency_test.c -o out/mlt.o
mpicc multiprocess_bandwith_test.c -o out/mbt.o

# # 4 slots per machine
# for i in 1 10 100 1000 10000 100000
# do
#    echo "Running single pair multiprocess_latency_test..."
#    mpirun -n 2 --hostfile hf_s4.txt -mca btl_tcp_if_include br0 ./out/mlt.o -m 100 -p $i >> csv/spmlt_s4.csv
# done

# for i in 1 10 100 1000 10000 100000
# do
#    echo "Running multiprocess_latency_test..."
#    mpirun -n 8 --hostfile hf_s4.txt -mca btl_tcp_if_include br0 ./out/mlt.o -m 100 -p $i >> csv/mlt_s4.csv
# done

# for i in 1 10 100 1000 10000 100000
# do
#    echo "Running single pair multiprocess_bandwith_test..."
#    mpirun -n 2 --hostfile hf_s4.txt -mca btl_tcp_if_include br0 ./out/mbt.o 100 $i 100 >> csv/spmbt_s4.csv
# done

# for i in 1 10 100 1000 10000 100000
# do
#    echo "Running multiprocess_bandwith_test..."
#    mpirun -n 8 --hostfile hf_s4.txt -mca btl_tcp_if_include br0 ./out/mbt.o 100 $i 100 >> csv/mbt_s4.csv
# done

# # 1 slot per machine
# for i in 1 10 100 1000 10000 100000
# do
#    echo "Running single pair multiprocess_latency_test..."
#    mpirun -n 2 --hostfile hf_s1.txt -mca btl_tcp_if_include br0 ./out/mlt.o -m 100 -p $i >> csv/spmlt_s1.csv
# done

# for i in 1 10 100 1000 10000 100000
# do
#    echo "Running multiprocess_latency_test..."
#    mpirun -n 8 --hostfile hf_s1.txt -mca btl_tcp_if_include br0 ./out/mlt.o -m 100 -p $i >> csv/mlt_s1.csv
# done

# for i in 1 10 100 1000 10000 100000
# do
#    echo "Running single pair multiprocess_bandwith_test..."
#    mpirun -n 2 --hostfile hf_s1.txt -mca btl_tcp_if_include br0 ./out/mbt.o 100 $i 100 >> csv/spmbt_s1.csv
# done

for i in 1 10 100 1000 10000 100000
do
   echo "Running multiprocess_bandwith_test..."
   mpirun -n 8 --hostfile hf_s1.txt -mca btl_tcp_if_include br0 ./out/mbt.o 100 $i 100 >> csv/mbt_s1.csv
done
