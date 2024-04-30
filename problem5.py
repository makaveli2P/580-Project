import random
import time
import matplotlib.pyplot as plt

# Function for Problem 2: Line Query Join
def line_query_join(relations):
    start_time = time.time()  # Record the start time

    num_relations = len(relations)  # Number of relations in the join query
    first_relation = relations[0]  # First relation in the join query
    intermediate_results = {}  # Dictionary to store intermediate join results
    final_result = []  # List to store the final join result

    # Build the initial dictionary using the first relation
    for tuple in first_relation:
        key = tuple[-1]  # Use the last attribute value as the key
        if key not in intermediate_results:
            intermediate_results[key] = [tuple[:-1]]  # Create a new list for a new key
        else:
            intermediate_results[key].append(tuple[:-1])  # Append the tuple (excluding the last attribute) to the
            # existing list

    # Perform the join with the remaining relations
    for rel_index in range(1, num_relations):
        new_intermediate_results = {}  # Dictionary for the current join step

        if rel_index != num_relations - 1:  # Not the last relation
            current_relation = relations[rel_index]  # Current relation
            for t in current_relation:
                key = t[0]  # Use the first attribute value as the key
                if key in intermediate_results:
                    for intermediate_tuple in intermediate_results[key]:
                        if t[1] not in new_intermediate_results:
                            new_tuple = intermediate_tuple + t[0:-1]  # Concatenate the intermediate tuple with the
                            # current tuple (excluding the last attribute)
                            new_intermediate_results[t[1]] = [new_tuple]  # Create a new list for a new key in the
                            # new dictionary
                        else:
                            new_intermediate_results[t[1]].append(
                                intermediate_tuple)  # Append the tuple to the existing list in the new dictionary
            intermediate_results = new_intermediate_results  # Update the intermediate dictionary for the next join step
        else:  # Last relation
            last_relation = relations[rel_index]  # Last relation
            for t in last_relation:
                key = t[0]  # Use the first attribute value as the key
                if key in intermediate_results:
                    for intermediate_tuple in intermediate_results[key]:
                        if t[1] not in new_intermediate_results:
                            new_tuple = intermediate_tuple + t[0:]  # Concatenate the intermediate tuple with the
                            # current tuple
                            final_result.append(new_tuple)  # Append the final tuple to the final result

    end_time = time.time()  # Record the end time
    execution_time = (end_time - start_time) * 1000  # Calculate the execution time in milliseconds

    return final_result, execution_time  # Return the final join result and the execution time
    # ... (same as in Problem 4)

# Function for Problem 3: Line Join Query
def line_join_query(relations):
    start_time = time.time()  # Record the start time

    k = len(relations)  # Number of relations in the join query
    H = [dict() for _ in range(k)]  # List of hash tables for each join step

    for i, Ri in enumerate(relations):
        if i == 0:  # First relation
            for t in Ri:
                key = t[1]  # Use the second attribute value as the key
                if key not in H[i]:
                    H[i][key] = []  # Create a new list for a new key
                H[i][key].append(t)  # Append the tuple to the corresponding list in the hash table
        else:  # Subsequent relations
            for t in Ri:
                key = t[0]  # Use the first attribute value as the key
                if key in H[i - 1]:  # Check if the key exists in the previous hash table
                    prev_tuples = H[i - 1][key]  # Get the tuples from the previous hash table
                    new_tuples = [prev_t + t[1:] for prev_t in prev_tuples]  # Concatenate the previous tuples with the current tuple
                    for new_t in new_tuples:
                        key = new_t[-1]  # Use the last attribute value as the key
                        if key not in H[i]:
                            H[i][key] = []  # Create a new list for a new key
                        H[i][key].append(new_t)  # Append the new tuple to the corresponding list in the current hash table

            print(f"R1-{i+1} = R1-{i} ⋈ R{i+1}")
            print("Intermediate Join Result:")
            for tuples in H[i].values():
                for tuple in tuples:
                    print(tuple)
            print()

    result = []
    for tuples in H[k - 1].values():  # Collect the final join result from the last hash table
        result.extend(tuples)

    end_time = time.time()  # Record the end time
    execution_time = (end_time - start_time) * 1000  # Calculate the execution time in milliseconds

    return result, execution_time  # Return the final join result and the execution time
    start_time = time.time()  # Record the start time

    k = len(relations)  # Number of relations in the join query
    H = [dict() for _ in range(k)]  # List of hash tables for each join step

    for i, Ri in enumerate(relations):
        if i == 0:  # First relation
            for t in Ri:
                key = t[1]  # Use the second attribute value as the key
                if key not in H[i]:
                    H[i][key] = []  # Create a new list for a new key
                H[i][key].append(t)  # Append the tuple to the corresponding list in the hash table
        else:  # Subsequent relations
            for t in Ri:
                key = t[0]  # Use the first attribute value as the key
                if key in H[i - 1]:  # Check if the key exists in the previous hash table
                    prev_tuples = H[i - 1][key]  # Get the tuples from the previous hash table
                    new_tuples = [prev_t + t[1:] for prev_t in prev_tuples]  # Concatenate the previous tuples with the current tuple
                    for new_t in new_tuples:
                        key = new_t[-1]  # Use the last attribute value as the key
                        if key not in H[i]:
                            H[i][key] = []  # Create a new list for a new key
                        H[i][key].append(new_t)  # Append the new tuple to the corresponding list in the current hash table

            print(f"R1-{i+1} = R1-{i} ⋈ R{i+1}")
            print("Intermediate Join Result:")
            for tuples in H[i].values():
                for tuple in tuples:
                    print(tuple)
            print()

    result = []
    for tuples in H[k - 1].values():  # Collect the final join result from the last hash table
        result.extend(tuples)

    end_time = time.time()  # Record the end time
    execution_time = (end_time - start_time) * 1000  # Calculate the execution time in milliseconds

    return result, execution_time  # Return the final join result and the execution time
    # ... (same as in Problem 4)

# Generate dataset for the 3-line join as described in Problem 5
R1 = [(i, 5) for i in range(1, 1001)] + [(i, 7) for i in range(1001, 2001)] + [(2001, 2002)]
random.shuffle(R1)  # Take a random permutation on the tuples in R1

R2 = [(5, i) for i in range(1, 1001)] + [(7, i) for i in range(1001, 2001)] + [(2002, 8)]
random.shuffle(R2)  # Take a random permutation on the tuples in R2

R3 = [(random.randint(2002, 3000), random.randint(1, 3000)) for _ in range(2000)] + [(8, 30)]
random.shuffle(R3)  # Take a random permutation on the tuples in R3

relations = [R1, R2, R3]

print("R1: ", "Length: ", len(R1), R1)
print("R2: ", "Length: ", len(R2), R2)
print("R3: ", "Length: ", len(R3), R3)

# Run the join queries and print the results with execution times
print("\n================ Running Line Query Join From Problem 2: ========================")
result_problem2, time_problem2 = line_query_join(relations)
print("\nJoin Result:")
for tuple in result_problem2:
    print(tuple)
print("Execution Time (Problem 2):", time_problem2, "milliseconds")

print("\n================ Running Hash Join From Problem 3: ==============================")
result_problem3, time_problem3 = line_join_query(relations)
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