numRows = 5
pt = [[1]]

for i in range(numRows - 1):
    temp = [0] + pt[-1] + [0]
    row = []
    for j in range(len(pt[-1]) + 1):
        row.append(temp[j] + temp[j+1])
    pt.append(row)

print(pt)

