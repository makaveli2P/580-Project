from collections import defaultdict
def line_query_join_p2(relations):
    k = len(relations)
    r1 = relations[0]
    intermediate_hash = {}
    join_result = []
    for i in range(len(r1)):
        key = r1[i][-1]
        if key not in intermediate_hash:
            intermediate_hash[key] = [r1[i][:-1]]
        else:
            intermediate_hash[key].append(r1[i][:-1])
    for rel_index in range(1, k - 1):
        relation = relations[rel_index]
        new_hash = defaultdict(list)
        for t in relation:
            if t[0] in intermediate_hash:
                new_hash[t[-1]].extend(tuple + t[0:len(t) - 1] for tuple in intermediate_hash[t[0]])
        intermediate_hash = new_hash
    relation = relations[k-1]
    join_result = [tuple + t[0:] for t in relation if t[0] in intermediate_hash for tuple in intermediate_hash[t[0]]]
    return join_result
