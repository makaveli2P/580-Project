import time

# Sample relations R1 and R2
R1 = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11)]
R2 = [(2, 20), (3, 30), (4, 40), (5, 50), (6, 60), (7, 70), (8, 80), (9, 90), (10, 100), (11, 110)]


def nested_loop_join(R1, R2):
    """
    Performs a nested loop join on relations R1 and R2.
    Returns the joined tuples (A, B, C) where R1.B = R2.B.
    """
    join_result = []  # Initialize an empty list to store the joined tuples

    start_time = time.time()  # Record the start time

    for t1 in R1:  # Iterate over each tuple t1 in relation R1
        a1 = t1[0]  # Extract the value of attribute A from t1
        b1 = t1[1]  # Extract the value of attribute B from t1

        for t2 in R2:  # Iterate over each tuple t2 in relation R2
            b2 = t2[0]  # Extract the value of attribute B from t2
            c2 = t2[1]  # Extract the value of attribute C from t2

            if b1 == b2:  # Check if the B attribute values match
                join_result.append((a1, b2, c2))  # Append the joined tuple (A, B, C) to the result

    end_time = time.time()  # Record the end time
    execution_time = (end_time - start_time) * 1000  # Calculate the execution time in milliseconds
    return join_result, execution_time  # Return the list of joined tuples and the execution time


query_result_brute, time_brute = nested_loop_join(R1, R2)  # Call the nested_loop_join function with R1 and R2

# Print results for the brute-force nested loop join
print("Results from nested loop join (R1.B = R2.B):")
for a, b, c in query_result_brute:
    print(f"({a}, {b}, {c})")
print(f"Execution time: {time_brute:.6f} milliseconds")


def join_using_hashing(R1, R2):
    """
    Performs a join operation on relations R1 and R2 using a hash table.
    Returns the joined tuples (A, B, C) where R1.B = R2.B.
    """
    hash_table = {}  # Initialize an empty hash table

    start_time = time.time()  # Record the start time

    # Build the hash table using tuples from R1
    for a, b in R1:
        if b not in hash_table:
            hash_table[b] = []  # Create a new list for a new B value
        hash_table[b].append((a, b))  # Append the tuple (A, B) to the list for the corresponding B value

    result = []  # Initialize an empty list to store the joined tuples

    # Probe the hash table using tuples from R2
    for b, c in R2:
        if b in hash_table:  # Check if the B value from R2 exists in the hash table
            for a, b_prime in hash_table[b]:  # Iterate over the tuples with matching B value in the hash table
                result.append((a, b_prime, c))  # Append the joined tuple (A, B, C) to the result

    end_time = time.time()  # Record the end time
    execution_time = (end_time - start_time) * 1000  # Calculate the execution time in milliseconds
    return result, execution_time  # Return the list of joined tuples and the execution time


query_result_hash, time_hash = join_using_hashing(R1, R2)  # Call the join_using_hashing function with R1 and R2

# Print results for the join using hashing
print("\nResults from join using hashing (R1.B = R2.B):")
for a, b, c in query_result_hash:
    print(f"({a}, {b}, {c})")
print(f"Execution time: {time_hash:.6f} milliseconds")
