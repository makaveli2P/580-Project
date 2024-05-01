import random
import time
import matplotlib.pyplot as plt
from join_functions import line_query_join_p2, line_join_query_p3

# Generate random dataset for the 3-line join
R1 = [(i, random.randint(1, 5000)) for i in range(1, 101)]
R2 = [(random.randint(1, 5000), j) for j in range(1, 101)]
R3 = [(l, l) for l in range(1, 101)]
relations = [R1, R2, R3]

print("R1:", "Length:", len(R1), R1)
print("R2:", "Length:", len(R2), R2)
print("R3:", "Length:", len(R3), R3)

# Run the join queries and print the results with execution times
print("\n================ Running Line Query Join From Problem 2: ========================")
result_problem2, time_problem2 = line_query_join_p2(relations)
print("\nJoin Result:")
for tuple in result_problem2:
    print(tuple)
print("Execution Time (Problem 2):", time_problem2, "milliseconds")

print("\n================ Running Hash Join From Problem 3: ==============================")
result_problem3, time_problem3 = line_join_query_p3(relations)
print("\nJoin Result:")
for tuple in result_problem3:
    print(tuple)
print("Execution Time (Problem 3):", time_problem3, "milliseconds")

# Visualize the results using matplotlib
fig, ax = plt.subplots()
ax.bar(['Problem 2', 'Problem 3'], [time_problem2, time_problem3])
ax.set_ylabel('Execution Time (milliseconds)')
ax.set_title('Execution Time Comparison')
plt.show()