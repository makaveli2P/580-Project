import pandas as pd


def compare_results(file1, file2):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    return df1.equals(df2)

result_comparison = compare_results('p2_result.csv', 'p3_2_result.csv')
result_comparison_2 = compare_results('p2_result.csv', 'Q6_results_2.csv')

if result_comparison:
    print("Results from p2 and p3_2 are the same.")
else:
    print("Results from p2 and p3_2 are different.")
if result_comparison_2:
    print("Results from p2 and MySql are the same. Hence all three results are the same.")
else:
    print("Results from p2 and MySql are not the same. Hence all three results are not the same.")
