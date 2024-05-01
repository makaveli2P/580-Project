import time


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


R1 = [(1, 2), (2, 3), (3, 4), (4, 5)]
R2 = [(2, 6), (3, 7), (4, 8), (5, 9)]
R3 = [(6, 10), (7, 11), (8, 12), (9, 13)]
R4 = [(10, 14), (11, 15), (12, 16), (13, 17)]
R5 = [(14, 18), (15, 19), (16, 20), (17, 21)]

relations = [R1, R2, R3, R4, R5]

result, execution_time = line_join_query(relations)

print("Final Join Result:")
for tuple in result:
    print(tuple)
print(f"Execution Time: {execution_time:.6f} milliseconds")
