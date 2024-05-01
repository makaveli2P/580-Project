from p3.P3_2 import line_join_query_p3_2
R1 = [(1, 2), (2, 3), (3, 4), (4, 5)]
R2 = [(2, 6), (3, 7), (4, 8), (5, 9)]
R3 = [(6, 10), (7, 11), (8, 12), (9, 13)]

relations = [R1, R2, R3]

result = line_join_query_p3_2(relations)
print("Final Join Result:")
for tuple in result:
    print(tuple)