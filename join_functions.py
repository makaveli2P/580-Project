import time

def line_query_join_p2(relations):
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
    # ... (same code as before)

def line_join_query_p3(relations):
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
    # ... (same code as before)