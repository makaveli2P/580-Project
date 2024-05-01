# 580-Project
## Directory Structure
```
.
├── Q1.py
├── Q2.py
├── Q3.py
├── Q4.py
├── Q5.py
├── Q6.py
├── Q6_results_2.csv
├── README.md
├── Runtime_comparison_p4.png
├── Runtime_comparison_p4_2.png
├── Runtime_comparison_p5.png
├── compare_results.py
├── main.py
├── p2
│   ├── P2.py
├── p2_result.csv
├── p3
│   ├── P3_1.py
│   ├── P3_2.py
├── p3_2_result.csv
```
## Setup Instructions

1. Clone the repository into your local environment.
```
git clone https://github.com/makaveli2P/580-Project.git
```

2. Open the folder in PyCharm or navigate to the folder using the command line.

## File Descriptions and Usage

- **Problem1.py**: Contains the solution for problem 1. This file contains implementation of two algorithms.Run the file in PyCharm or use the command:
```
python Q1.py
```


- **Q2.py**: Contains the solution for problem 2. This file contains the implementation required for problem 2. Run the file in PyCharm or use the command:

```
python Q2.py
```
- **Q3.py**: Contains the solution for problem 3. This file contains implmentation of the algorithm in problem 1 for a line query. Run the file in PyCharm or use the command:

```
python Q3.py
```
- **Q4.py**: Contains the solution for problem 4. This file contains comparison fo the implementation 2 and 3 for a dataset given in the problem 4. Run the file in PyCharm or use the command:

```
python Q4.py
```

- **Q5.py**: Contains the solution for problem 5. This file contains comparison fo the implementation 2 and 3 for a dataset given in the problem 5. Run the file in PyCharm or use the command:

```
python Q5.py
```

- **Q6.py**: This file contains comparison fo the implementation 2 and 3 for a dataset given in the problem 4. Change the MySQL credentials in the code and run the file, or use the command:

```
python Q6.py
#For MySQL query
USE Q6;

SELECT R1.i,  R2.value, R3.x, R3.y
FROM R1
JOIN R2 ON R1.value = R2.value
JOIN R3 ON R2.i = R3.x;

```
- **compare_results.py**: Contains the comparison between the CSV files obtained from Q6.
```
python compare_results.py
```
