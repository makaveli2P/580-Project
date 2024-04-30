import random
import time
import matplotlib.pyplot as plt
from problem2 import line_query_join
from problem3 import line_join_query

# Generate random dataset for the 3-line join
R1 = [(i, random.randint(1, 5000)) for i in range(1, 101)]
R2 = [(random.randint(1, 5000), j) for j in range(1, 101)]
R3 = [(l, l) for l in range(1, 101)]
relations = [R1, R2, R3]

# Run the join queries using the imported functions
print("Running Line Query Join (Problem 2):")
result_problem2, time_problem2 = line_query_join(relations)
print("Final Join Result (Problem 2):")
for tuple in result_problem2:
    print(tuple)
print("Execution Time (Problem 2):", time_problem2, "milliseconds")

print("\nRunning Hash Join (Problem 3):")
result_problem3, time_problem3 = line_join_query(relations)
print("Final Join Result (Problem 3):")
for tuple in result_problem3:
    print(tuple)
print("Execution Time (Problem 3):", time_problem3, "milliseconds")

# Visualize the results using matplotlib
fig, ax = plt.subplots()
ax.bar(['Problem 2 (Line Query Join)', 'Problem 3 (Hash Join)'], [time_problem2, time_problem3])
ax.set_ylabel('Execution Time (milliseconds)')
ax.set_title('Execution Time Comparison')
plt.show()