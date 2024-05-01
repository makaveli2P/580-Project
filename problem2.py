import time


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


# Sample relations
R1 = [(1, 2), (2, 3), (3, 4), (4, 5)]
R2 = [(2, 6), (3, 7), (4, 8), (5, 9)]
R3 = [(6, 10), (7, 11), (8, 12), (9, 13)]
R4 = [(10, 14), (11, 15), (12, 16), (13, 17)]
R5 = [(14, 18), (15, 19), (16, 20), (17, 21)]

relations = [R1, R2, R3, R4, R5]

result, execution_time = line_query_join(relations)

print("Joined Query:")
for i in result:
    print(i)
print(f"Execution Time: {execution_time:.6f} milliseconds")
