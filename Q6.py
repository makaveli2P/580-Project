import mysql.connector
import random
import csv
import pandas as pd
from p2.P2 import line_query_join_p2
# from p3.P3_2 import line_join_query_p3_2
import time
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
    end_time = time.time()  # Record the end time
    execution_time = (end_time - start_time)  # Calculate the execution time in milliseconds
    return join_result,execution_time

      # Return the final join result and the execution time
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

    result = []
    for tuples in H[k - 1].values():  # Collect the final join result from the last hash table
        result.extend(tuples)

    end_time = time.time()  # Record the end time
    execution_time = (end_time - start_time)   # Calculate the execution time in milliseconds

    return result, execution_time  # Return the final join result and the execution time
# Connect to MySQL (replace 'username' and 'password' with your MySQL credentials)
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Pf717984#",
  database="Q6" # Replace 'your_database_name' with your database name
)

# Create a cursor object to interact with the database
mycursor = mydb.cursor()

# Create tables R1, R2, R3
mycursor.execute("DROP TABLE IF EXISTS R1")
mycursor.execute("DROP TABLE IF EXISTS R2")
mycursor.execute("DROP TABLE IF EXISTS R3")
mycursor.execute("CREATE TABLE IF NOT EXISTS R1 (i INT, value INT)")
mycursor.execute("CREATE TABLE IF NOT EXISTS R2 (value INT, i INT)")
mycursor.execute("CREATE TABLE IF NOT EXISTS R3 (x INT, y INT)")

# Generate tuples for relation R1
R1_tuples = [(i, 5) for i in range(1, 1001)] + [(i, 7) for i in range(1001, 2001)] + [(2001, 2002)]
random.shuffle(R1_tuples)

# Insert tuples into table R1
for tuple in R1_tuples:
    sql = "INSERT INTO R1 (i, value) VALUES (%s, %s)"
    val = (tuple[0], tuple[1])
    mycursor.execute(sql, val)

# Generate tuples for relation R2
R2_tuples = [(5, i) for i in range(1, 1001)] + [(7, i) for i in range(1001, 2001)] + [(2002, 8)]
random.shuffle(R2_tuples)

# Insert tuples into table R2
for tuple in R2_tuples:
    sql = "INSERT INTO R2 (value, i) VALUES (%s, %s)"
    val = (tuple[0], tuple[1])
    mycursor.execute(sql, val)

# Generate tuples for relation R3
R3_tuples = [(random.randint(2002, 3000), random.randint(1, 3000)) for _ in range(2000)] + [(8, 30)]
random.shuffle(R3_tuples)

# Insert tuples into table R3
for tuple in R3_tuples:
    sql = "INSERT INTO R3 (x, y) VALUES (%s, %s)"
    val = (tuple[0], tuple[1])
    mycursor.execute(sql, val)


p2_times = []
p3_2_times = []

start_time = time.time()
p2_result, runtime_p2 = line_query_join_p2([R1_tuples, R2_tuples, R3_tuples])
end_time = time.time()
p2_times.append(end_time - start_time)
start_time = time.time()
p3_2_result, runtime_p3 = line_join_query_p3([R1_tuples, R2_tuples, R3_tuples])
end_time = time.time()
p3_2_times.append(end_time - start_time)
print(len(p3_2_result))
print(len(p2_result))


avg_p2_time_micro = runtime_p2
avg_p3_2_time_micro = runtime_p3

print("Runtime time for Implementation 2: {:.11f} seconds".format(avg_p2_time_micro))
print("Runtime time for Implementation 3: {:.11f} seconds".format(avg_p3_2_time_micro))

mydb.commit()

mydb.close()

# Write results of p2 to CSV
with open('p2_result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(p2_result)

# Write results of p3_2 to CSV
with open('p3_2_result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(p3_2_result)

# Compare the results

