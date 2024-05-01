# def hash_join(R1, R2, index_R1, index_R2):
#     hash_table = {}
#     for r in R1:
#         hash_key = r[index_R1]
#         if hash_key not in hash_table:
#             hash_table[hash_key] = []
#         hash_table[hash_key].append(r)
#     join_result = []
#     for r in R2:
#         hash_key = r[index_R2]
#         if hash_key in hash_table:
#             for s in hash_table[hash_key]:
#                 s = s[0:len(s)-1]
#                 join_result.append(s + r)
#     return join_result
#
#
# def iterative_line_join(relations):
#     result = relations[0]
#     for i in range(1, len(relations)):
#         result = hash_join(result, relations[i], -1, 0)
#     return result
#
#
# R1 = [(1, 2), (2, 3), (3, 4)]
# R2 = [(2, 5), (3, 6), (4, 7)]
# R3 = [(5, 8), (6, 9), (7, 10)]
# R4 = [(8, 11), (9, 12), (10, 13)]
#
# k = iterative_line_join([R1, R2,R3,R4])
# print(k)

def line_join_query(relations):
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
    print(H)
    result = []
    for tuples in H[k - 1].values():
        result.extend(tuples)

    return result


R1 = [(1, 2), (2, 3), (3, 4), (4, 5)]
R2 = [(2, 6), (3, 7), (4, 8), (5, 9)]
R3 = [(6, 10), (7, 11), (8, 12), (9, 13)]
R4 = [(10, 14), (11, 15), (12, 16), (13, 17)]
R5 = [(14, 18), (15, 19), (16, 20), (17, 21)]

relations = [R1, R2, R3, R4, R5]

result = line_join_query(relations)
print("Join Result:")
for tuple in result:
    print(tuple)