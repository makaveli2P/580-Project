from p2.P2 import line_query_join_p2

R1 = [(1, 2), (2, 3), (3, 4), (4, 5)]
R2 = [(2, 6), (3, 7), (4, 8), (5, 9)]
R3 = [(6, 10), (7, 11), (8, 12), (9, 13)]
R4 = [(10, 14), (11, 15), (12, 16), (13, 17)]
R5 = [(14, 18), (15, 19), (16, 20), (17, 21)]

relations = [R1, R2, R3, R4, R5]

result = line_query_join_p2(relations)

print("Joined_query from Implementation 2:")
for i in result:
    print(i)