def line_join_query_p3_brute_force(relations):
    # Assuming all relations have the same number of attributes
    # k = len(relations)
    result = []

    # Brute force join
    for tuple1 in relations[0]:
        for tuple2 in relations[1]:
            if tuple1[1] == tuple2[0]:  # Join condition
                for tuple3 in relations[2]:
                    if tuple2[1] == tuple3[0]:  # Join condition
                        result.append(tuple1 + tuple2[1:] + tuple3[1:])

    return result




