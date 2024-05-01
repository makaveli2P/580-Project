def line_join_query_p3_2(relations):
    k = len(relations)
    H = [dict() for _ in range(k)]
    for i, Ri in enumerate(relations):
        if i == 0:
            for t in Ri:
                key = t[1]
                if key not in H[i]:
                    H[i][key] = []
                H[i][key].append(t)
        else:
            for t in Ri:
                key = t[0]
                if key in H[i - 1]:
                    prev_tuples = H[i - 1][key]
                    new_tuples = [prev_t + t[1:] for prev_t in prev_tuples]
                    for new_t in new_tuples:
                        key = new_t[-1]
                        if key not in H[i]:
                            H[i][key] = []
                        H[i][key].append(new_t)

    result = []
    for tuples in H[k - 1].values():
        result.extend(tuples)

    return result

