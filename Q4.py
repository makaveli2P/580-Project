import random
from p2.P2 import line_query_join_p2
from p3.P3_1 import line_join_query_p3_brute_force
from p3.P3_2 import line_join_query_p3_2
import time
import matplotlib.pyplot as plt

# Define the number of epochs
epochs = 100  # You can adjust this value based on how many epochs you want to run

# Lists to store execution times
p2_times = []
p3_times = []



for _ in range(epochs):
    # Generate relation R1
    R1 = [(i, random.randint(1, 5000)) for i in range(1, 101)]

    # Generate relation R2
    R2 = [(random.randint(1, 5000), j) for j in range(1, 101)]

    # Generate relation R3
    R3 = [(l, l) for l in range(1, 101)]

    # Time execution of p2_result
    start_time = time.time()
    p2_result = line_query_join_p2([R1, R2, R3])
    end_time = time.time()
    p2_times.append(end_time - start_time)
    print("*" * 50)
    print("The result from implementation 2:")
    print("*" * 50)
    for i in p2_result:
        print(i)
    print("\n")


    start_time = time.time()
    p3_result = line_join_query_p3_2([R1, R2, R3])
    end_time = time.time()
    p3_times.append(end_time - start_time)
    print("*" * 50)
    print("The result from implementation 3:")
    print("*" * 50)
    for i in p3_result:
        print(i)
    print("\n")

# Calculate average times
avg_p2_time = sum(p2_times) / epochs
avg_p3_time = sum(p3_times) / epochs


avg_p2_time_micro = avg_p2_time * 10**6
avg_p3_time_micro = avg_p3_time * 10**6

print("Average time for p2_result: {:.11f} microseconds".format(avg_p2_time_micro))
print("Average time for p3_result: {:.11f} microseconds".format(avg_p3_time_micro))

# Plotting the comparison
plt.figure(figsize=(12, 6))

# Function names
functions = ['p2_result',   'p3_2_result']

# Average times in microseconds
avg_times_micro = [avg_p2_time_micro, avg_p3_time_micro]

plt.bar(functions, avg_times_micro, color=['blue', 'orange'])
plt.xlabel('Functions')
plt.ylabel('Average Time (microseconds) over 10000 epochs')
plt.title('Comparison of Average Execution Times')
plt.savefig("Runtime_comparison_p4_2.png")
# plt.show()
