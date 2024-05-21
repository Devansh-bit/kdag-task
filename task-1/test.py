import pandas as pd
import numpy as np

excel_vals = pd.read_excel('TaskData.xlsx', header=None).values
num_words = len(excel_vals)

words = []
options = ['doctor', 'lawyer', 'teacher', 'engineer', 'accountant', 'nurse', 'police', 'architect', 'dentist', 'pharmacist']
for i in range(num_words):
    words.append(excel_vals[i][0].replace("'", "").strip().lower())

def lev(a, b, i, j, matrix):
    if matrix[i-1][j-1] != -1:
        return matrix[i-1][j-1]
    if min(i, j) == 0:
        return max(i, j)
    return min(
        lev(a, b, i-1, j, matrix) + 1,
        lev(a, b, i, j-1, matrix) + 1,
        lev(a, b, i-1, j-1, matrix) + (1 if a[i-1] != b[j-1] else 0) 
    )
def lev_distance(a, b):
    matrix = np.full((len(a), len(b)), -1, dtype=np.int32)
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            matrix[i][j] = lev(a,b,i+1,j+1, matrix)
    return matrix[len(a)-1][len(b)-1]


correct_words_lev = []
option_counter = [0] * len(options)

i = 0
for word in words:
    for option in options:
        i += 1
        lev_distance(word, option)