from p3.P3_2 import line_join_query_p3_2
from p3.P3_1 import line_join_query_p3_brute_force

R1 = [(1, 2), (2, 3), (3, 4), (4, 5)]
R2 = [(2, 6), (3, 7), (4, 8), (5, 9)]
R3 = [(6, 10), (7, 11), (8, 12), (9, 13)]
R4 = [(10, 14), (11, 15), (12, 16), (13, 17)]
R5 = [(14, 18), (15, 19), (16, 20), (17, 21)]

relations = [R1, R2, R3, R4, R5]

result = line_join_query_p3_2(relations)
print("Joined_query from Implementation 3:")
for tuple in result:
    print(tuple)

# result = line_join_query_p3_brute_force(relations)
# print("Joined_query from Implementation 3 (Brute Force):")
# for tuple in resultn :
#     print(tuple)
