#!/bin/python3

import re

n,m = map(int, input().rstrip().split())

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

st = ""
for i in range(m):
    for j in range(n):
        st += matrix[j][i]

reg = r'\b(\W+)\b'
fin = re.sub(reg," ",st)
print(fin)
